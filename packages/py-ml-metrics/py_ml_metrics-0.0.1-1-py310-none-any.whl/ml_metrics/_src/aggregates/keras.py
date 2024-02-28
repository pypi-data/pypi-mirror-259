# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""TF metric wrapper."""

import collections
import dataclasses
import importlib
import itertools
from typing import Any, Dict, Iterable, List, Optional, Tuple, Type, Union, Protocol, runtime_checkable

import apache_beam as beam
from ml_metrics._src.aggregates import base as agg
import numpy as np
import tensorflow as tf
from tensorflow_model_analysis import constants
from tensorflow_model_analysis.metrics import binary_confusion_matrices
from tensorflow_model_analysis.metrics import metric_types
from tensorflow_model_analysis.metrics import metric_util
from tensorflow_model_analysis.metrics import tf_metric_accumulators
from tensorflow_model_analysis.proto import config_pb2
from tensorflow_model_analysis.utils import model_util


@runtime_checkable
class KerasMetric(Protocol):

  def reset_state(self):
    """Resets all of the metric state variables."""

  def update_state(self, *args, **kwargs):
    """Accumulates statistics for the metric."""
    
  def merge_states(self, states: Any) -> Any:
    """Merges metric states."""

  def result(self):
    """Computes and returns the metric value tensor."""


@dataclasses.dataclass(frozen=True)
class KerasAggregateFn(agg.AggregateFn):
  metric: KerasMetric

  def create_state(self):
    self.metric.reset_state()
    return self.metric
  
  def update_state(self, state: Any, *inputs: Any, **named_inputs: Any):
    self.metric.update_state(*inputs, **named_inputs)
    return self.metric
  
  def merge_states(self, states: Any) -> Any:
    iter_states = iter(states)
    result = next(iter_states)
    for state in iter_states:
      result.merge_states(state)
    return result
    
    self.metric.merge_states(states)
    return self.metric
  
  def get_result(self, state: Any) -> Any:
    return self.metric.result()



_CONFIG_KEY = 'config'
_NUM_THRESHOLDS_KEY = 'num_thresholds'
_THRESHOLDS_KEY = 'thresholds'
_CLASS_ID_KEY = 'class_id'
_TOP_K_KEY = 'top_k'
_DEFAULT_NUM_THRESHOLDS_IN_KERAS = 200

_TFMetricOrLoss = Union[tf.keras.metrics.Metric, tf.keras.losses.Loss]



def _filter_duplicate_metrics(
    metrics: Dict[str, List[tf.keras.metrics.Metric]],
    model_name: str,
    sub_key: Optional[metric_types.SubKey] = None,
) -> Dict[str, List[tf.keras.metrics.Metric]]:
  """Filters duplicate metrics from the metrics."""
  for output_name, metrics_list in metrics.items():
    unique_metrics = {}
    for metric in metrics_list:
      key = metric_types.MetricKey(
          name=metric.name,
          model_name=model_name,
          output_name=output_name,
          sub_key=_verify_and_update_sub_key(model_name, output_name, sub_key,
                                             metric))
      # Replace any previous metric (i.e. last added metric wins).
      unique_metrics[key] = metric
    metrics[output_name] = list(unique_metrics.values())
  return metrics


def _sparse_metrics(
    metrics: Dict[str, List[tf.keras.metrics.Metric]]
) -> Dict[str, List[tf.keras.metrics.Metric]]:
  """Returns input metrics filtered to contain only the sparse metrics."""
  results = {}
  for k, v in metrics.items():
    for m in v:
      if m.__class__.__name__.startswith('Sparse'):
        if k not in results:
          results[k] = []
        results[k].append(m)
  return results


def _verify_and_update_sub_key(model_name: str, output_name: str,
                               sub_key: metric_types.SubKey,
                               metric: _TFMetricOrLoss):
  """Verifies the multi-class metric key matches settings used by the metric."""
  if hasattr(metric, _CLASS_ID_KEY) and metric.class_id is not None:
    if sub_key and sub_key.class_id != metric.class_id:
      raise ValueError(
          '{} tf.keras.metric has class_id = {}, but the metric is being added '
          'using sub_key = {}: model_name={}, output_name={}'.format(
              metric.name, metric.class_id, sub_key, model_name, output_name))
    return metric_types.SubKey(class_id=metric.class_id)
  elif hasattr(metric, _TOP_K_KEY) and metric.top_k is not None:
    if sub_key and sub_key.top_k != metric.top_k:
      raise ValueError(
          '{} tf.keras.metric has top_k = {}, but the metric is being added '
          'using sub_key = {}: model_name={}, output_name={}'.format(
              metric.name, metric.top_k, sub_key, model_name, output_name))
    return metric_types.SubKey(top_k=metric.top_k)
  else:
    return sub_key


def _deserialize_metrics(
    metric_configs: List[Dict[str, Any]]) -> List[tf.keras.metrics.Metric]:
  return [
      metric_util.deserialize_metric(c, use_legacy_format=True)
      for c in metric_configs
  ]


def _deserialize_losses(
    loss_configs: List[Dict[str, Any]]) -> List[tf.keras.losses.Loss]:
  return [
      metric_util.deserialize_loss(c, use_legacy_format=True)
      for c in loss_configs
  ]


def _custom_objects(
    metrics: Dict[str, List[tf.keras.metrics.Metric]]) -> List[Tuple[str, str]]:
  """Returns list of (module, class_name) tuples for custom objects."""
  custom_objects = []
  for metric_list in metrics.values():
    for metric in metric_list:
      if (metric.__class__.__module__ != tf.keras.metrics.__name__ and
          metric.__class__.__module__ != tf.keras.losses.__name__):
        custom_objects.append(
            (metric.__class__.__module__, metric.__class__.__name__))
  return custom_objects


def _load_custom_objects(
    custom_objects: List[Tuple[str, str]]) -> Dict[str, Type[Any]]:
  """Loads custom metric options."""
  loaded_custom_objects = {}
  for module_name, class_name in custom_objects:
    module = importlib.import_module(module_name)
    loaded_custom_objects[class_name] = getattr(module, class_name)
  return loaded_custom_objects


def _get_config_value(key: str, metric_config: Dict[str, Any]) -> Optional[Any]:
  """Returns value for key within config or None."""
  if _CONFIG_KEY in metric_config and key in metric_config[_CONFIG_KEY]:
    return metric_config[_CONFIG_KEY][key]
  return None


def _wrap_confusion_matrix_metric(
    metric: tf.keras.metrics.Metric, eval_config: config_pb2.EvalConfig,
    model_name: str, output_name: str, sub_key: Optional[metric_types.SubKey],
    aggregation_type: Optional[metric_types.AggregationType],
    class_weights: Optional[Dict[int, float]],
    example_weighted: bool) -> metric_types.MetricComputations:
  """Returns confusion matrix metric wrapped in a more efficient computation."""

  # Special handling for AUC metric which supports aggregation inherently via
  # multi_label flag.
  if (isinstance(metric, tf.keras.metrics.AUC) and
      hasattr(metric, 'label_weights')):
    if metric.label_weights:
      if class_weights:
        raise ValueError(
            'class weights are configured in two different places: (1) via the '
            'tf.keras.metrics.AUC class (using "label_weights") and (2) via '
            'the MetricsSpecs (using "aggregate.class_weights"). Either remove '
            'the label_weights settings in the AUC class or remove the '
            'class_weights from the AggregationOptions: metric={}, '
            'class_weights={}'.format(metric, class_weights))
      class_weights = {i: v for i, v in enumerate(metric.label_weights)}
    if metric.multi_label:
      raise NotImplementedError('AUC.multi_label=True is not implemented yet.')

  sub_key = _verify_and_update_sub_key(model_name, output_name, sub_key, metric)
  key = metric_types.MetricKey(
      name=metric.name,
      model_name=model_name,
      output_name=output_name,
      aggregation_type=aggregation_type,
      sub_key=sub_key,
      example_weighted=example_weighted)

  metric_config = metric_util.serialize_metric(metric, use_legacy_format=True)

  thresholds = None
  num_thresholds = None
  # The top_k metrics have special settings. If we are setting the top_k value
  # outside of keras (i.e. using BinarizeOptions), then we need to set the
  # special threshold ourselves otherwise the default threshold of 0.5 is used.
  if (sub_key and sub_key.top_k is not None and
      _get_config_value(_TOP_K_KEY, metric_config) is None and
      _get_config_value(_THRESHOLDS_KEY, metric_config) is None and
      _get_config_value(_NUM_THRESHOLDS_KEY, metric_config) is None):
    thresholds = [float('-inf')]
  elif hasattr(metric, _THRESHOLDS_KEY):
    thresholds = metric.thresholds
  # Only one of either thresholds or num_thresholds should be used. Keras AUC
  # allows both but thresholds has more precedence.
  if thresholds is None and hasattr(metric, _NUM_THRESHOLDS_KEY):
    num_thresholds = metric.num_thresholds

  # Make sure matrices are calculated.
  computations = binary_confusion_matrices.binary_confusion_matrices(
      num_thresholds=num_thresholds,
      thresholds=thresholds,
      eval_config=eval_config,
      model_name=model_name,
      output_name=output_name,
      sub_key=sub_key,
      aggregation_type=aggregation_type,
      class_weights=class_weights,
      example_weighted=example_weighted)
  matrices_key = computations[-1].keys[-1]

  def result(
      metrics: Dict[metric_types.MetricKey, Any]
  ) -> Dict[metric_types.MetricKey, Any]:
    """Returns result derived from binary confusion matrices."""
    matrices = metrics[matrices_key]

    metric = metric_util.deserialize_metric(
        metric_config, use_legacy_format=True
    )
    if (
        isinstance(metric, tf.keras.metrics.AUC)
        or isinstance(metric, tf.keras.metrics.SpecificityAtSensitivity)
        or isinstance(metric, tf.keras.metrics.SensitivityAtSpecificity)
    ):
      metric.true_positives.assign(np.array(matrices.tp))
      metric.true_negatives.assign(np.array(matrices.tn))
      metric.false_positives.assign(np.array(matrices.fp))
      metric.false_negatives.assign(np.array(matrices.fn))
    elif isinstance(metric, tf.keras.metrics.Precision):
      metric.true_positives.assign(np.array(matrices.tp))
      metric.false_positives.assign(np.array(matrices.fp))
    elif isinstance(metric, tf.keras.metrics.Recall):
      metric.true_positives.assign(np.array(matrices.tp))
      metric.false_negatives.assign(np.array(matrices.fn))
    elif isinstance(metric, tf.keras.metrics.TruePositives):
      metric.accumulator.assign(np.array(matrices.tp))
    elif isinstance(metric, tf.keras.metrics.FalsePositives):
      metric.accumulator.assign(np.array(matrices.fp))
    elif isinstance(metric, tf.keras.metrics.TrueNegatives):
      metric.accumulator.assign(np.array(matrices.tn))
    elif isinstance(metric, tf.keras.metrics.FalseNegatives):
      metric.accumulator.assign(np.array(matrices.fn))
    return {key: metric.result().numpy()}

  derived_computation = metric_types.DerivedMetricComputation(
      keys=[key], result=result)
  computations.append(derived_computation)
  return computations


class _LossMetric(tf.keras.metrics.Mean):
  """Converts a loss function into a metric."""

  def __init__(self, loss, name=None, dtype=None):
    if name is None:
      name = loss.name
    super().__init__(name=name, dtype=dtype)
    self.loss = loss

  def update_state(self, y_true, y_pred, sample_weight):  # pytype: disable=signature-mismatch  # overriding-parameter-count-checks
    return super().update_state(
        self.loss(y_true, y_pred), sample_weight=sample_weight)


class _CompilableMetricsCombiner(beam.CombineFn):
  """Combines compilable metric weights and computes result."""

  # TODO(b/173811366): Consider removing the desired_batch_size knob and
  # only use input size.
  def __init__(self,
               metric_configs: Dict[str, List[Dict[str, Any]]],
               loss_configs: Dict[str, List[Dict[str, Any]]],
               custom_objects: List[Tuple[str, str]],
               eval_config: Optional[config_pb2.EvalConfig],
               model_name: Optional[str],
               sub_key: Optional[metric_types.SubKey],
               aggregation_type: Optional[metric_types.AggregationType],
               class_weights: Dict[int, float],
               example_weighted: bool,
               desired_batch_size: Optional[int] = None):
    # Use parallel lists to store output_names and configs to guarantee
    # consistent ordering and for natural alignment with the accumulator where
    # lists are used instead of dicts for efficency.
    self._eval_config = eval_config
    self._model_name = model_name
    self._output_names = sorted(metric_configs)
    self._metric_configs = [metric_configs[n] for n in self._output_names]
    self._loss_configs = [loss_configs[n] for n in self._output_names]
    self._custom_objects = custom_objects
    self._sub_key = sub_key
    self._aggregation_type = aggregation_type
    self._class_weights = class_weights
    self._example_weighted = example_weighted
    # True if the sub_key is part of the metric config already (i.e. top_k).
    self._sub_key_in_config = sub_key and sub_key.top_k is not None
    for cfg in itertools.chain.from_iterable(metric_configs.values()):
      if _get_config_value(_TOP_K_KEY, cfg) is None:
        self._sub_key_in_config = False
        break
    self._metrics = None  # type: Dict[str, List[tf.keras.metrics.Metric]]
    self._desired_batch_size = desired_batch_size
    self._batch_size_beam_metric = (
        beam.metrics.Metrics.distribution(
            constants.METRICS_NAMESPACE,
            'keras_compilable_metrics_combine_batch_size'))
    self._total_input_byte_size_beam_metric = beam.metrics.Metrics.distribution(
        constants.METRICS_NAMESPACE,
        'keras_compilable_metrics_combine_batch_bytes_size')
    self._num_compacts = beam.metrics.Metrics.counter(
        constants.METRICS_NAMESPACE, 'num_compacts')

  def setup(self):
    if self._metrics is None:
      self._metrics = {}
      with tf.keras.utils.custom_object_scope(
          _load_custom_objects(self._custom_objects)):
        for i, output_name in enumerate(self._output_names):
          self._metrics[output_name] = (
              _deserialize_metrics(self._metric_configs[i]))
          for loss in _deserialize_losses(self._loss_configs[i]):
            self._metrics[output_name].append(_LossMetric(loss))

  def _process_batch(
      self, accumulator: tf_metric_accumulators.TFCompilableMetricsAccumulator):
    if accumulator.len_inputs() == 0:
      return
    self._batch_size_beam_metric.update(accumulator.len_inputs())
    self._total_input_byte_size_beam_metric.update(
        accumulator.get_size_estimate())
    for output_index, output_name in enumerate(self._output_names):
      inputs = accumulator.get_inputs(output_index)
      for metric_index, metric in enumerate(self._metrics[output_name]):
        try:
          metric.reset_states()
          metric.update_state(*inputs)
        except Exception as e:
          raise ValueError(
              f'TF Metric {metric.name} fails to update with inputs:\n{inputs},'
              f'\nMetric full config: {metric.get_config()}'
          ) from e
        accumulator.add_weights(output_index, metric_index,
                                metric.get_weights())
    accumulator.clear_inputs()

  def create_accumulator(
      self) -> tf_metric_accumulators.TFCompilableMetricsAccumulator:
    configs = zip(self._metric_configs, self._loss_configs)
    padding_options = None
    if self._eval_config is not None:
      model_spec = model_util.get_model_spec(self._eval_config,
                                             self._model_name)
      if model_spec is not None and model_spec.HasField('padding_options'):
        padding_options = model_spec.padding_options

    return tf_metric_accumulators.TFCompilableMetricsAccumulator(
        padding_options, [len(m) + len(l) for m, l in configs],
        desired_batch_size=self._desired_batch_size)

  def add_input(
      self, accumulator: tf_metric_accumulators.TFCompilableMetricsAccumulator,
      element: metric_types.StandardMetricInputs
  ) -> tf_metric_accumulators.TFCompilableMetricsAccumulator:
    for i, output_name in enumerate(self._output_names):
      # When micro averaging is being used, flatten should be set to True so
      # that each class is treated as though it was an independent example.
      micro_average = (
          self._aggregation_type and self._aggregation_type.micro_average)
      for label, prediction, example_weight in (
          metric_util.to_label_prediction_example_weight(
              element,
              eval_config=self._eval_config,
              model_name=self._model_name,
              output_name=output_name,
              # Skip sub_key processing if part of the keras config
              sub_key=self._sub_key if not self._sub_key_in_config else None,
              aggregation_type=self._aggregation_type,
              class_weights=self._class_weights,
              example_weighted=self._example_weighted,
              flatten=micro_average)):
        # Keras requires non-sparse keys for its calcuations.
        if self._sub_key_in_config and label.shape != prediction.shape:
          label = metric_util.one_hot(label, prediction)
        accumulator.add_input(i, label, prediction, example_weight)
    if accumulator.should_flush():
      self._process_batch(accumulator)
    return accumulator

  def merge_accumulators(
      self, accumulators: Iterable[
          tf_metric_accumulators.TFCompilableMetricsAccumulator]
  ) -> tf_metric_accumulators.TFCompilableMetricsAccumulator:
    accumulators = iter(accumulators)
    result = next(accumulators)
    self._process_batch(result)
    for accumulator in accumulators:
      # Finish processing last batch
      self._process_batch(accumulator)
      # Merge the weights
      for output_index, output_name in enumerate(self._output_names):
        for metric_index in range(len(self._metrics[output_name])):
          weights = accumulator.get_weights(output_index, metric_index)
          if weights is None:
            # It is possible for beam to create an accumulator but pass no
            # inputs to it resulting in in empty weights. In theory all weights
            # should be empty but we check on a per metric weights basis.
            continue
          result.add_weights(output_index, metric_index, weights)
    return result

  def compact(
      self, accumulator: tf_metric_accumulators.TFCompilableMetricsAccumulator
  ) -> tf_metric_accumulators.TFCompilableMetricsAccumulator:
    self._process_batch(accumulator)
    self._num_compacts.inc(1)
    return accumulator

  def extract_output(
      self, accumulator: tf_metric_accumulators.TFCompilableMetricsAccumulator
  ) -> Dict[metric_types.MetricKey, Any]:
    self._process_batch(accumulator)

    def make_metric_key(metric_name, output_name):
      return metric_types.MetricKey(
          name=metric_name,
          model_name=self._model_name,
          output_name=output_name,
          sub_key=self._sub_key,
          example_weighted=self._example_weighted)

    result = {}
    for output_index, output_name in enumerate(self._output_names):
      for metric_index, metric in enumerate(self._metrics[output_name]):

        weights = accumulator.get_weights(output_index, metric_index)
        if weights is not None:
          metric.set_weights(weights)
        else:
          metric.reset_states()
        metric_result = metric.result()
        if isinstance(metric_result, dict):
          for name, value in metric_result.items():
            key = make_metric_key(f'{metric.name}/{name}', output_name)
            result[key] = value.numpy()
        else:
          key = make_metric_key(metric.name, output_name)
          result[key] = metric_result.numpy()
    return result
