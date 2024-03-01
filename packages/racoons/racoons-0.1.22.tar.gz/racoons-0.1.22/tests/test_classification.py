import numpy as np
import pytest

from racoons.models import classifiers
from racoons.models.validation import (
    get_param_grid,
    cross_validate_model,
    get_feature_importance,
    metrics_from_cv_result
)
from racoons.models.model_builder import build_model
from racoons.models.classification import (
    multivariate_classification,
    grid_search_multivariate_classification,
    univariate_classification, single_shot_classification,
)
from racoons.visualization import plot_feature_importances, plot_roc_curve_from_cv_metrics
from racoons.data_utils import features_and_targets_from_dataframe


def test_feature_importance(classification_data, classification_data_with_missing_values):
    for data in [classification_data, classification_data_with_missing_values]:
        df, target_cols, feature_cols = data
        X, y, scale_levels = features_and_targets_from_dataframe(
            df, feature_cols, target_cols
        )

        sample_method = "smote"
        feature_selection_method = "lasso"
        estimator_name = "logistic_regression"

        if X.isnull().values.any():
            print("Features containing missing values. Using XGBClassifier to handle those.")
            estimator_name = "xgboost"
            feature_selection_method = None
            sample_method = None

        model = build_model(
            scale_levels, sample_method, feature_selection_method, estimator_name
        )

        model.fit(X, y)
        feature_importance = get_feature_importance(model)
        assert (
            feature_importance.columns.tolist()
            == model["estimator"].feature_names_in_.tolist()
        )
        assert not feature_importance.empty


class TestClassification:
    def test_cross_validate_model(self, classification_data, classification_data_with_missing_values):
        for data in [classification_data, classification_data_with_missing_values]:
            df, target_cols, feature_cols = data
            X, y, scale_levels = features_and_targets_from_dataframe(
                df, feature_cols, target_cols
            )

            sample_method = "smote"
            feature_selection_method = "lasso"
            estimator_name = "random_forest"

            if X.isnull().values.any():
                print("Features containing missing values. Using XGBClassifier to handle those.")
                estimator_name = "xgboost"
                feature_selection_method = None
                sample_method = None

            model = build_model(
                scale_levels, sample_method, feature_selection_method, estimator_name
            )

            # Test the cross_validate_model function
            tprs, aucs_preds, aucs_probs, f1_scores, feature_importances = cross_validate_model(
                model, X, y["outcome"]
            )

            # Check if the output lists have the correct lengths (10 folds)
            assert len(tprs) == len(aucs_preds) == len(f1_scores) == 10

            # Check if feature importances is not empty
            assert not feature_importances.empty

            # Check if each element in the lists is a NumPy array
            assert all(isinstance(tpr, np.ndarray) for tpr in tprs)
            assert all(isinstance(auc_, np.float64) for auc_ in aucs_preds)
            assert all(isinstance(f1_score_, np.float64) for f1_score_ in f1_scores)

    def test_multivariate_classification(
        self, classification_data, classification_data_with_missing_values, output_path, tmp_path
    ):
        out_path = tmp_path
        for data in [classification_data, classification_data_with_missing_values]:
            df, target_cols, feature_cols = data

            feature_selection_method = "lasso"
            sample_method = "smote"

            if df[feature_cols].isnull().values.any():
                print("Features containing missing values. Cant use feature selection and sampling.")
                feature_selection_method = None
                sample_method = None

            result_df = multivariate_classification(
                df=df,
                feature_cols=feature_cols,
                target_cols=target_cols,
                feature_selection_method=feature_selection_method,
                sample_method=sample_method,
                estimators=classifiers.keys(),
                output_path=out_path,
            )

            # Validate the result
            if df[feature_cols].isnull().values.any():
                assert len(result_df) == len(target_cols)
            else:
                assert len(result_df) == len(target_cols) * len(classifiers)
            assert not result_df.empty

    def test_univariate_classification(
        self, classification_data, classification_data_with_missing_values, tmp_path, output_path
    ):
        out_path = tmp_path
        for data in [classification_data, classification_data_with_missing_values]:
            df, target_cols, feature_cols = data

            sample_method = "smote"

            if df[feature_cols].isnull().values.any():
                print("Features containing missing values. Cant use feature selection and sampling.")
                sample_method = None

            result_df = univariate_classification(
                df=df,
                feature_cols=feature_cols,
                target_cols=target_cols,
                sample_method=sample_method,
                estimators=classifiers.keys(),
                output_path=out_path,
            )

            # Validate the result
            if df[feature_cols].isnull().values.any():
                assert len(result_df) == len(target_cols) * len(feature_cols)
            else:
                assert len(result_df) == len(target_cols) * len(classifiers) * len(feature_cols)
            assert not result_df.empty

    def test_single_shot_classification(
        self, classification_data, classification_data_with_missing_values, output_path, tmp_path
    ):
        out_path = tmp_path
        for data in [classification_data, classification_data_with_missing_values]:
            df, target_cols, feature_cols = data

            feature_selection_method = None
            sample_method = "smote"

            if df[feature_cols].isnull().values.any():
                print("Features containing missing values. Cant use feature selection and sampling.")
                feature_selection_method = None
                sample_method = None

            result_df = single_shot_classification(
                df=df,
                feature_cols=feature_cols,
                target_cols=target_cols,
                feature_selection_method=feature_selection_method,
                sample_method=sample_method,
                estimators=classifiers.keys(),
                output_path=out_path,
            )

            # Validate the result
            if df[feature_cols].isnull().values.any():
                assert len(result_df) == len(target_cols)
            else:
                assert len(result_df) == len(target_cols) * len(classifiers)
            assert not result_df.empty


class TestGridSearchClassification:
    def test_get_param_grid(self, classification_data, classification_data_with_missing_values):
        for classifier_name, classifier in classifiers.items():
            for data in [classification_data, classification_data_with_missing_values]:
                df, target_cols, feature_cols = data
                X, y, scale_levels = features_and_targets_from_dataframe(
                    df, feature_cols, target_cols
                )
                sample_method = "smote"
                feature_selection_method = "lasso"
                classifier_name = classifier_name

                if X.isnull().values.any():
                    print("Features containing missing values. Using XGBClassifier to handle those.")
                    classifier_name = "xgboost"
                    feature_selection_method = None
                    sample_method = None

                model = build_model(
                    feature_scale_levels=scale_levels,
                    feature_selection_method=feature_selection_method,
                    sample_method=sample_method,
                    estimator_name=classifier_name,
                )
                param_grid = get_param_grid(model)

                if classifier_name == "logistic_regression":
                    assert "estimator__penalty" in param_grid
                    assert "estimator__solver" in param_grid
                    assert "estimator__C" in param_grid
                elif classifier_name == "random_forest":
                    assert "estimator__n_estimators" in param_grid
                    assert "estimator__n_jobs" in param_grid
                elif classifier_name == "ada_boost":
                    assert "estimator__learning_rate" in param_grid
                    assert "estimator__n_estimators" in param_grid
                elif classifier_name == "gradient_boosting":
                    assert "estimator__learning_rate" in param_grid
                    assert "estimator__n_estimators" in param_grid
                elif classifier_name == "decision_tree":
                    assert "estimator__criterion" in param_grid
                elif classifier_name == "xgboost":
                    assert "estimator__n_estimators" in param_grid
                # elif classifier_name == "k_neighbors":
                #     assert "estimator__n_neighbors" in param_grid
                #     assert "estimator__n_jobs" in param_grid

                model = build_model(
                    feature_scale_levels=scale_levels,
                    feature_selection_method="lasso",
                    sample_method="smote",
                    estimator_name=classifier_name,
                )
                param_grid = get_param_grid(model)
                if feature_selection_method is not None:
                    assert "feature_selection__estimator__C" in param_grid
                    assert "feature_selection__estimator__solver" in param_grid

    def test_grid_search_classification(
        self, classification_data, classification_data_with_missing_values, tmp_path, output_path
    ):
        for data in [classification_data, classification_data_with_missing_values]:
            df, target_cols, feature_cols = data
            out_path = tmp_path
            sample_method = "smote"
            feature_selection_method = "lasso"
            classifier_name = classifiers.keys()

            if df[feature_cols].isnull().values.any():
                print("Features containing missing values. Using XGBClassifier to handle those.")
                classifier_name = "xgboost"
                feature_selection_method = None
                sample_method = None
            result_df = grid_search_multivariate_classification(
                df=df,
                feature_cols=feature_cols,
                target_cols=target_cols,
                feature_selection_method=feature_selection_method,
                sample_method=sample_method,
                estimators=classifier_name,
                output_path=out_path,
            )

            # Validate the result
            assert len(result_df) == len(target_cols)
            assert not result_df.empty
