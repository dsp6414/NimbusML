# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
FastTreesTweedieRegressor
"""

__all__ = ["FastTreesTweedieRegressor"]


from ...entrypoints.trainers_fasttreetweedieregressor import \
    trainers_fasttreetweedieregressor
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignatureWithRoles


class FastTreesTweedieRegressor(
        BasePipelineItem,
        DefaultSignatureWithRoles):
    """

    Machine Learning Fast Tree

    .. remarks::
        Trains gradient boosted decision trees to fit target values using a
        Tweedie loss function. This learner is a generalization of Poisson,
        compound Poisson, and gamma regression.


        **Reference**

            `Wikipedia: Gradient boosting (Gradient tree boosting)
            <https://en.wikipedia.org/wiki/Gradient_boosting#Gradient_tree_boosting>`_

            `Greedy function approximation: A gradient boosting machine.
            <http://projecteuclid.org/DPubS?service=UI&version=1.0&verb=Display&handle=euclid.aos/1013203451>`_

    :param num_trees: Specifies the total number of decision trees to create in
        the ensemble. By creating more decision trees, you can potentially get
        better coverage, but the training time increases.

    :param num_leaves: The maximum number of leaves (terminal nodes) that can
        be created in any tree. Higher values potentially increase the size of
        the tree and get better precision, but risk overfitting and requiring
        longer training times.

    :param min_split: Minimum number of training instances required to form a
        leaf. That is, the minimal number of documents allowed in a leaf of
        regression tree, out of the sub-sampled data. A 'split' means that
        features in each level of the tree (node) are randomly divided.

    :param learning_rate: Determines the size of the step taken in the
        direction of the gradient in each step of the learning process.  This
        determines how fast or slow the learner converges on the optimal
        solution. If the step size is too big, you might overshoot the optimal
        solution.  If the step size is too small, training takes longer to
        converge to the best solution.

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

    :param index: Index parameter for the Tweedie distribution, in the range
        [1, 2]. 1 is Poisson loss, 2 is gamma loss, and intermediate values are
        compound Poisson loss.

    :param best_step_trees: Use best regression step trees?.

    :param use_line_search: Should we use line search for a step size.

    :param num_post_bracket_steps: Number of post-bracket line search steps.

    :param min_step_size: Minimum line search step size.

    :param optimizer: Default is ``sgd``.

    :param early_stopping_rule: Early stopping rule. (Validation set (/valid)
        is required.).

    :param early_stopping_metrics: Early stopping metrics. (For regression, 1:
        L1, 2:L2; for ranking, 1:NDCG@1, 3:NDCG@3).

    :param enable_pruning: Enable post-training pruning to avoid overfitting.
        (a validation set is required).

    :param use_tolerant_pruning: Use window and tolerance for pruning.

    :param pruning_threshold: The tolerance threshold for pruning.

    :param pruning_window_size: The moving window size for pruning.

    :param shrinkage: Shrinkage.

    :param dropout_rate: Dropout rate for tree regularization.

    :param get_derivatives_sample_rate: Sample each query 1 in k times in the
        GetDerivatives function.

    :param write_last_ensemble: Write the last ensemble instead of the one
        determined by early stopping.

    :param max_tree_output: Upper bound on absolute value of single tree
        output.

    :param random_start: Training starts from random ordering (determined by
        /r1).

    :param filter_zero_lambdas: Filter zero lambdas during training.

    :param baseline_scores_formula: Freeform defining the scores that should be
        used as the baseline ranker.

    :param baseline_alpha_risk: Baseline alpha for tradeoffs of risk (0 is
        normal training).

    :param position_discount_freeform: The discount freeform which specifies
        the per position discounts of documents in a query (uses a single
        variable P for position where P=0 is first position).

    :param parallel_trainer: Allows to choose Parallel FastTree Learning
        Algorithm.

    :param train_threads: The number of threads to use.

    :param random_state: The seed of the random number generator.

    :param feature_select_seed: The seed of the active feature selection.

    :param entropy_coefficient: The entropy (regularization) coefficient
        between 0 and 1.

    :param histogram_pool_size: The number of histograms in the pool (between 2
        and numLeaves).

    :param disk_transpose: Whether to utilize the disk or the data's native
        transposition facilities (where applicable) when performing the
        transpose.

    :param feature_flocks: Whether to collectivize features during dataset
        preparation to speed up training.

    :param categorical_split: Whether to do split based on multiple categorical
        feature values.

    :param max_categorical_groups_per_node: Maximum categorical split groups to
        consider when splitting on a categorical feature. Split groups are a
        collection of split points. This is used to reduce overfitting when
        there many categorical features.

    :param max_categorical_split_points: Maximum categorical split points to
        consider when splitting on a categorical feature.

    :param min_docs_percentage_split: Minimum categorical docs percentage in a
        bin to consider for a split.

    :param min_docs_for_categorical_split: Minimum categorical doc count in a
        bin to consider for a split.

    :param bias: Bias for calculating gradient for each feature bin for a
        categorical feature.

    :param bundling: Bundle low population bins. Bundle.None(0): no bundling,
        Bundle.AggregateLowPopulation(1): Bundle low population,
        Bundle.Adjacent(2): Neighbor low population bundle.

    :param num_bins: Maximum number of distinct values (bins) per feature.

    :param sparsify_threshold: Sparsity level needed to use sparse feature
        representation.

    :param first_use_penalty: The feature first use penalty coefficient. This
        is a form of regularization that incurs a penalty for using a new
        feature when creating the tree. Increase this value to create trees
        that don't use many features.

    :param feature_reuse_penalty: The feature re-use penalty (regularization)
        coefficient.

    :param gain_conf_level: Tree fitting gain confidence requirement (should be
        in the range [0,1) ).

    :param softmax_temperature: The temperature of the randomized softmax
        distribution for choosing the feature.

    :param execution_times: Print execution time breakdown to stdout.

    :param feature_fraction: The fraction of features (chosen randomly) to use
        on each iteration.

    :param bagging_size: Number of trees in each bag (0 for disabling bagging).

    :param example_fraction: Percentage of training examples used in each bag.

    :param split_fraction: The fraction of features (chosen randomly) to use on
        each split.

    :param smoothing: Smoothing paramter for tree regularization.

    :param allow_empty_trees: When a root split is impossible, allow training
        to proceed.

    :param feature_compression_level: The level of feature compression to use.

    :param compress_ensemble: Compress the tree Ensemble.

    :param max_trees_after_compression: Maximum Number of trees after
        compression.

    :param test_frequency: Calculate metric values for train/valid/test every k
        rounds.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:func:`FastForestRegressor
        <nimbusml.ensemble.FastForestRegressor>`,
        :py:func:`FastTreesBinaryClassifier
        <nimbusml.ensemble.FastTreesBinaryClassifier>`,

    .. index:: models, regression

    Example:
       .. literalinclude:: /../nimbusml/examples/FastTreesTweedieRegressor.py
              :language: python

    """

    @trace
    def __init__(
            self,
            num_trees=100,
            num_leaves=20,
            min_split=10,
            learning_rate=0.2,
            normalize='Auto',
            caching='Auto',
            index=1.5,
            best_step_trees=False,
            use_line_search=False,
            num_post_bracket_steps=0,
            min_step_size=0.0,
            optimizer='GradientDescent',
            early_stopping_rule=None,
            early_stopping_metrics=0,
            enable_pruning=False,
            use_tolerant_pruning=False,
            pruning_threshold=0.004,
            pruning_window_size=5,
            shrinkage=1.0,
            dropout_rate=0.0,
            get_derivatives_sample_rate=1,
            write_last_ensemble=False,
            max_tree_output=100.0,
            random_start=False,
            filter_zero_lambdas=False,
            baseline_scores_formula=None,
            baseline_alpha_risk=None,
            position_discount_freeform=None,
            parallel_trainer=None,
            train_threads=None,
            random_state=123,
            feature_select_seed=123,
            entropy_coefficient=0.0,
            histogram_pool_size=-1,
            disk_transpose=None,
            feature_flocks=True,
            categorical_split=False,
            max_categorical_groups_per_node=64,
            max_categorical_split_points=64,
            min_docs_percentage_split=0.001,
            min_docs_for_categorical_split=100,
            bias=0.0,
            bundling='None',
            num_bins=255,
            sparsify_threshold=0.7,
            first_use_penalty=0.0,
            feature_reuse_penalty=0.0,
            gain_conf_level=0.0,
            softmax_temperature=0.0,
            execution_times=False,
            feature_fraction=1.0,
            bagging_size=0,
            example_fraction=0.7,
            split_fraction=1.0,
            smoothing=0.0,
            allow_empty_trees=True,
            feature_compression_level=1,
            compress_ensemble=False,
            max_trees_after_compression=-1,
            test_frequency=2147483647,
            **params):
        BasePipelineItem.__init__(
            self, type='regressor', **params)

        self.num_trees = num_trees
        self.num_leaves = num_leaves
        self.min_split = min_split
        self.learning_rate = learning_rate
        self.normalize = normalize
        self.caching = caching
        self.index = index
        self.best_step_trees = best_step_trees
        self.use_line_search = use_line_search
        self.num_post_bracket_steps = num_post_bracket_steps
        self.min_step_size = min_step_size
        self.optimizer = optimizer
        self.early_stopping_rule = early_stopping_rule
        self.early_stopping_metrics = early_stopping_metrics
        self.enable_pruning = enable_pruning
        self.use_tolerant_pruning = use_tolerant_pruning
        self.pruning_threshold = pruning_threshold
        self.pruning_window_size = pruning_window_size
        self.shrinkage = shrinkage
        self.dropout_rate = dropout_rate
        self.get_derivatives_sample_rate = get_derivatives_sample_rate
        self.write_last_ensemble = write_last_ensemble
        self.max_tree_output = max_tree_output
        self.random_start = random_start
        self.filter_zero_lambdas = filter_zero_lambdas
        self.baseline_scores_formula = baseline_scores_formula
        self.baseline_alpha_risk = baseline_alpha_risk
        self.position_discount_freeform = position_discount_freeform
        self.parallel_trainer = parallel_trainer
        self.train_threads = train_threads
        self.random_state = random_state
        self.feature_select_seed = feature_select_seed
        self.entropy_coefficient = entropy_coefficient
        self.histogram_pool_size = histogram_pool_size
        self.disk_transpose = disk_transpose
        self.feature_flocks = feature_flocks
        self.categorical_split = categorical_split
        self.max_categorical_groups_per_node = max_categorical_groups_per_node
        self.max_categorical_split_points = max_categorical_split_points
        self.min_docs_percentage_split = min_docs_percentage_split
        self.min_docs_for_categorical_split = min_docs_for_categorical_split
        self.bias = bias
        self.bundling = bundling
        self.num_bins = num_bins
        self.sparsify_threshold = sparsify_threshold
        self.first_use_penalty = first_use_penalty
        self.feature_reuse_penalty = feature_reuse_penalty
        self.gain_conf_level = gain_conf_level
        self.softmax_temperature = softmax_temperature
        self.execution_times = execution_times
        self.feature_fraction = feature_fraction
        self.bagging_size = bagging_size
        self.example_fraction = example_fraction
        self.split_fraction = split_fraction
        self.smoothing = smoothing
        self.allow_empty_trees = allow_empty_trees
        self.feature_compression_level = feature_compression_level
        self.compress_ensemble = compress_ensemble
        self.max_trees_after_compression = max_trees_after_compression
        self.test_frequency = test_frequency

    @property
    def _entrypoint(self):
        return trainers_fasttreetweedieregressor

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            feature_column=self._getattr_role('feature_column', all_args),
            label_column=self._getattr_role('label_column', all_args),
            weight_column=self._getattr_role('weight_column', all_args),
            group_id_column=self._getattr_role('group_id_column', all_args),
            num_trees=self.num_trees,
            num_leaves=self.num_leaves,
            min_documents_in_leafs=self.min_split,
            learning_rates=self.learning_rate,
            normalize_features=self.normalize,
            caching=self.caching,
            index=self.index,
            best_step_ranking_regression_trees=self.best_step_trees,
            use_line_search=self.use_line_search,
            num_post_bracket_steps=self.num_post_bracket_steps,
            min_step_size=self.min_step_size,
            optimization_algorithm=self.optimizer,
            early_stopping_rule=self.early_stopping_rule,
            early_stopping_metrics=self.early_stopping_metrics,
            enable_pruning=self.enable_pruning,
            use_tolerant_pruning=self.use_tolerant_pruning,
            pruning_threshold=self.pruning_threshold,
            pruning_window_size=self.pruning_window_size,
            shrinkage=self.shrinkage,
            dropout_rate=self.dropout_rate,
            get_derivatives_sample_rate=self.get_derivatives_sample_rate,
            write_last_ensemble=self.write_last_ensemble,
            max_tree_output=self.max_tree_output,
            random_start=self.random_start,
            filter_zero_lambdas=self.filter_zero_lambdas,
            baseline_scores_formula=self.baseline_scores_formula,
            baseline_alpha_risk=self.baseline_alpha_risk,
            position_discount_freeform=self.position_discount_freeform,
            parallel_trainer=self.parallel_trainer,
            num_threads=self.train_threads,
            rng_seed=self.random_state,
            feature_select_seed=self.feature_select_seed,
            entropy_coefficient=self.entropy_coefficient,
            histogram_pool_size=self.histogram_pool_size,
            disk_transpose=self.disk_transpose,
            feature_flocks=self.feature_flocks,
            categorical_split=self.categorical_split,
            max_categorical_groups_per_node=self.max_categorical_groups_per_node,
            max_categorical_split_points=self.max_categorical_split_points,
            min_docs_percentage_for_categorical_split=self.min_docs_percentage_split,
            min_docs_for_categorical_split=self.min_docs_for_categorical_split,
            bias=self.bias,
            bundling=self.bundling,
            max_bins=self.num_bins,
            sparsify_threshold=self.sparsify_threshold,
            feature_first_use_penalty=self.first_use_penalty,
            feature_reuse_penalty=self.feature_reuse_penalty,
            gain_confidence_level=self.gain_conf_level,
            softmax_temperature=self.softmax_temperature,
            execution_times=self.execution_times,
            feature_fraction=self.feature_fraction,
            bagging_size=self.bagging_size,
            bagging_train_fraction=self.example_fraction,
            split_fraction=self.split_fraction,
            smoothing=self.smoothing,
            allow_empty_trees=self.allow_empty_trees,
            feature_compression_level=self.feature_compression_level,
            compress_ensemble=self.compress_ensemble,
            max_trees_after_compression=self.max_trees_after_compression,
            test_frequency=self.test_frequency)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)