# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
OrdinaryLeastSquaresRegressor
"""

__all__ = ["OrdinaryLeastSquaresRegressor"]


from ...entrypoints.trainers_ordinaryleastsquaresregressor import \
    trainers_ordinaryleastsquaresregressor
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignatureWithRoles


class OrdinaryLeastSquaresRegressor(
        BasePipelineItem,
        DefaultSignatureWithRoles):
    """

    Train an OLS regression model

    .. remarks::
        `Ordinary least squares (OLS)
        <https://en.wikipedia.org/wiki/Ordinary_least_squares>`_ is a
        parameterized
        regression method. It assumes that the conditional mean of the
        dependent variable follows a linear function of
        the dependent variables. By minimizing the squares of the difference
        between observed values and the
        predictions, the parameters of the regressor can be estimated.


        **Reference**

            `Ordinary least squares (OLS)
            <https://en.wikipedia.org/wiki/Ordinary_least_squares>`_


    :param normalize: Specifies the type of automatic normalization used:

        * ``"Auto"``: if normalization is needed, it is performed
          automatically. This is the default choice.
        * ``"No"``: no normalization is performed.
        * ``"Yes"``: normalization is performed.
        * ``"Warn"``: if normalization is needed, a warning
          message is displayed, but normalization is not performed.

        Normalization rescales disparate data ranges to a standard scale.
        Feature
        scaling insures the distances between data points are proportional
        and
        enables various optimization methods such as gradient descent to
        converge
        much faster. If normalization is performed, a ``MaxMin`` normalizer
        is
        used. It normalizes values in an interval [a, b] where ``-1 <= a <=
        0``
        and ``0 <= b <= 1`` and ``b - a = 1``. This normalizer preserves
        sparsity by mapping zero to zero.

    :param caching: Whether learner should cache input training data.

    :param l2_weight: L2 regularization weight.

    :param per_parameter_significance: Whether to calculate per parameter
        significance statistics.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:func:`FastLinearRegressor
        <nimbusml.linear_model.FastLinearRegressor>`,
        :py:func:`LightGbmRegressor <nimbusml.ensemble.LightGbmRegressor>`,
        :py:func:`FastForestRegressor <nimbusml.ensemble.FastForestRegressor>`,
        :py:func:`FastTreesRegressor <nimbusml.ensemble.FastTreesRegressor>`,
        :py:func:`GamRegressor <nimbusml.ensemble.GamRegressor>`.

    .. index:: models, regression, linear

    Example:
       .. literalinclude:: /../nimbusml/examples/OrdinaryLeastSquaresRegressor.py
              :language: python
    """

    @trace
    def __init__(
            self,
            normalize='Auto',
            caching='Auto',
            l2_weight=1e-06,
            per_parameter_significance=True,
            **params):
        BasePipelineItem.__init__(
            self, type='regressor', **params)

        self.normalize = normalize
        self.caching = caching
        self.l2_weight = l2_weight
        self.per_parameter_significance = per_parameter_significance

    @property
    def _entrypoint(self):
        return trainers_ordinaryleastsquaresregressor

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            feature_column=self._getattr_role('feature_column', all_args),
            label_column=self._getattr_role('label_column', all_args),
            weight_column=self._getattr_role('weight_column', all_args),
            normalize_features=self.normalize,
            caching=self.caching,
            l2_weight=self.l2_weight,
            per_parameter_significance=self.per_parameter_significance)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)
