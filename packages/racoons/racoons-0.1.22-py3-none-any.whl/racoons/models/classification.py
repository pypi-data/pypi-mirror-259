from datetime import datetime

import pandas as pd
from matplotlib import pyplot as plt
import sklearn
from pathlib import Path

from sklearn.metrics import roc_auc_score, roc_curve, f1_score
from sklearn.model_selection import train_test_split
from tqdm import tqdm

from racoons.models import classifiers
from racoons.data_utils import features_and_targets_from_dataframe
from racoons.models.model_builder import get_estimator, build_model
from racoons.reporting import make_report_df, update_report
from racoons.models.validation import (
    hyper_parameter_optimization,
    cross_validate_model,
    metrics_from_cv_result,
    get_feature_importance,
)
from racoons.visualization import (
    plot_feature_importances,
    plot_roc_curve_from_cv_metrics,
)

######################## OPEN ISSUES ##################################################
# TODO: refit on f1 in cross-validation
#######################################################################################

sklearn.set_config(transform_output="pandas")


def multivariate_classification(
        df: pd.DataFrame,
        feature_cols: list[str],
        target_cols: list[str],
        feature_selection_method: str,
        sample_method: str,
        estimators: list[str],
        output_path: Path | str,
):
    """
    Run a classification pipeline with cross-validation and save the results.

    Args:
        df (pd.DataFrame): The input DataFrame containing features and targets.
        feature_cols (List[str]): List of column names containing features.
        target_cols (List[str]): List of column names containing target variables.
        feature_selection_method (Optional[str]): The method for feature selection, if any.
        sample_method (Optional[str]): The method for addressing class imbalance, if any.
        estimators (List[str]): List of classifier names to use in the pipeline.
        output_path (Optional[Path]): Path to the output folder. Defaults to 'output'.
        **kwargs: Additional keyword arguments.

    Returns:
        pd.DataFrame: A DataFrame containing the results of the classification.

    Raises:
        Any specific exceptions or errors.

    Example:
        >>> result_df = multivariate_classification(
        ...     df=data_frame,
        ...     feature_cols=['feature1', 'feature2'],
        ...     target_cols=['target'],
        ...     feature_selection_method='lasso',
        ...     sample_method='smote',
        ...     estimators=['random_forest', 'logistic_regression'],
        ...     output_path=Path('results'),
        ... )

    Note:
        - The function runs a classification pipeline for each target column and each specified estimator.
        - Cross-validation is performed, and results including ROC-AUC and feature importance are saved.
        - The output is stored in the specified output_path.
    """
    # setup output folder
    output_path = Path(output_path)
    output_path.mkdir(exist_ok=True)
    output_folder = (
            output_path
            / f"multivariate_analysis_{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}"
    )
    output_folder.mkdir(exist_ok=True)

    # get features and targets
    features, targets, feature_scale_levels = features_and_targets_from_dataframe(
        df, feature_cols, target_cols
    )
    if features.isnull().values.any():
        print("Features containing missing values. Using XGBClassifier to handle those.")
        estimators = ["xgboost"]
        feature_selection_method = None
        sample_method = None

    # iterate over targets and features
    report_df = make_report_df(sample_method, feature_selection_method)
    with tqdm(total=(targets.shape[1]) * len(estimators)) as pbar:
        plot_index = 0
        for target in targets:
            for estimator in estimators:
                estimator_name = type(classifiers[estimator]).__name__
                model = build_model(
                    feature_scale_levels,
                    sample_method,
                    feature_selection_method,
                    estimator,
                )
                cv_result = cross_validate_model(model, features, df[target])
                cv_result_metrics = metrics_from_cv_result(cv_result)

                # roc-auc
                roc_curve_plot = plot_roc_curve_from_cv_metrics(
                    cv_result_metrics,
                    plot_title=f"Classification of \n {target} using " f"\n{estimator_name}",
                )
                roc_curve_plot_path = output_folder / (f"roc_auc_{plot_index}.png")
                roc_curve_plot.savefig(roc_curve_plot_path, dpi=600)
                plt.close(roc_curve_plot)

                # feature importance
                feature_importance = get_feature_importance(model)
                feature_importance_plot = plot_feature_importances(
                    feature_importance, title=f"Feature importance for classification of \n {target} \n"
                                              f"using \n {estimator_name}"
                )
                feature_importance_plot_path = output_folder / (
                    f"feature_importance_{plot_index}.png"
                )
                feature_importance_csv_path = output_folder / (
                    f"feature_importance_{plot_index}.csv"
                )
                feature_importance.to_csv(feature_importance_csv_path, sep=";")
                feature_importance_plot.savefig(feature_importance_plot_path, dpi=300)
                plt.close(feature_importance_plot)

                # save report
                selected_features = model["estimator"].feature_names_in_
                negative_samples = (~df[target]).sum()
                positive_samples = (df[target]).sum()
                mean_auc_preds = cv_result_metrics["mean_auc_preds"]
                std_auc_preds = cv_result_metrics["std_auc_preds"]
                mean_auc_probs = cv_result_metrics["mean_auc_probs"]
                std_auc_probs = cv_result_metrics["std_auc_probs"]
                mean_f1 = cv_result_metrics["mean_f1"]
                std_f1 = cv_result_metrics["std_f1"]

                report_df.loc[len(report_df.index)] = update_report(
                    target=target,
                    features=selected_features,
                    negative_samples=negative_samples,
                    positive_samples=positive_samples,
                    estimator_name=estimator_name,
                    mean_auc_preds=mean_auc_preds,
                    std_auc_preds=std_auc_preds,
                    mean_auc_probs=mean_auc_probs,
                    std_auc_probs=std_auc_probs,
                    mean_f1=mean_f1,
                    std_f1=std_f1,
                    roc_plot_path=roc_curve_plot_path,
                    feature_importance_csv=feature_importance_csv_path,
                    feature_importance_plot_path=feature_importance_plot_path,
                    sampling=sample_method,
                    feature_selection=feature_selection_method,
                    selected_features=selected_features,
                )
                pbar.update(1)
                plot_index += 1
            report_df.to_excel(output_folder / "report.xlsx")
            report_df.to_csv(output_folder / "report.csv", sep=";")

        report_df.to_excel(output_folder / "report.xlsx")
        report_df.to_csv(output_folder / "report.csv", sep=";")
        return report_df


def grid_search_multivariate_classification(
        df: pd.DataFrame,
        feature_cols: list[str],
        target_cols: list[str],
        feature_selection_method: str,
        sample_method: str,
        estimators: list[str],
        output_path: Path | str,
):
    """
    Perform grid search for hyperparameter optimization in a classification pipeline.

    This function conducts a grid search to find the optimal hyperparameters for each specified classifier
    while considering feature selection and sampling methods. The grid search is performed based on cross-validation
    metrics (AUC and F1 score) to evaluate the model's performance.

    Args:
        df (pd.DataFrame): The input dataframe containing features and targets.
        feature_cols (List[str]): List of column names representing the feature variables.
        target_cols (List[str]): List of column names representing the target variables.
        feature_selection_method (str): The method used for feature selection. Supported methods are 'lasso' and None.
        sample_method (str): The method used for handling class imbalance. Supported methods are 'smote', 'adasyn', and 'random_oversampling'.
        estimators (List[str]): List of classifiers to be evaluated during the grid search.
        output_path (Path): The output path where the results and plots will be saved.

    Returns:
        pd.DataFrame: A dataframe containing the results of the grid search, including key metrics and paths to relevant plots.

    Raises:
        None

    Example:
        >>> df = pd.DataFrame({'feature1': [1, 2, 3], 'target': [0, 1, 0]})
        >>> feature_cols = ['feature1']
        >>> target_cols = ['target']
        >>> feature_selection_method = 'lasso'
        >>> sample_method = 'smote'
        >>> estimators = ['random_forest', 'gradient_boosting']
        >>> output_path = Path('./output/')
        >>> result_df = grid_search_multivariate_classification(df, feature_cols, target_cols,
        ...                                       feature_selection_method, sample_method,
        ...                                       estimators, output_path)

    Note:
        This function performs grid search by evaluating the specified classifiers with various hyperparameters,
        considering the provided feature selection and sampling methods. It outputs a dataframe with the grid search results.
    """
    # setup output folder
    output_path = Path(output_path)
    output_path.mkdir(exist_ok=True)
    output_folder = (
            output_path
            / f"gs_multivariate_analysis_{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}"
    )
    output_folder.mkdir(exist_ok=True)

    # get features and targets
    features, targets, feature_scale_levels = features_and_targets_from_dataframe(
        df, feature_cols, target_cols
    )

    if features.isnull().values.any():
        print("Features containing missing values. Using XGBClassifier to handle those.")
        estimators = ["xgboost"]
        feature_selection_method = None
        sample_method = None

    # iterate over targets and features
    report_df = make_report_df(
        sample_method, feature_selection_method, grid_search=True
    )

    with tqdm(total=(targets.shape[1])) as pbar:
        # find best performing model by cross validation
        plot_index = 0
        for target in targets:
            cv_df = pd.DataFrame(columns=["Model", "AUC"])
            print("Initial cross-validation...")
            for estimator in estimators:
                # remove feature selection steps from model for initial cv
                model = build_model(
                    feature_scale_levels, sample_method, None, estimator
                )
                initial_cv_result = cross_validate_model(
                    model, features, df[target]
                )

                cv_result_metrics = metrics_from_cv_result(initial_cv_result)
                cv_df.loc[len(cv_df.index)] = [
                    estimator,
                    cv_result_metrics["mean_auc_preds"],
                ]
            print("Done.")
            best_cv_estimator = cv_df.sort_values(by="AUC", ascending=False)[
                "Model"
            ].iloc[0]
            grid_search_model = build_model(
                feature_scale_levels,
                sample_method,
                feature_selection_method,
                best_cv_estimator,
            )
            print("Hyper-parameter optimization...")
            best_params, mean_score, std_score = hyper_parameter_optimization(
                grid_search_model,
                features,
                df[target],
            )
            print("done.")
            # run cross valiadtion with best model
            optimized_model = build_model(
                feature_scale_levels,
                sample_method,
                feature_selection_method,
                best_cv_estimator,
            )
            optimized_model.set_params(**best_params)
            cv_result = cross_validate_model(
                optimized_model, features, df[target]
            )
            cv_result_metrics = metrics_from_cv_result(cv_result)

            # roc-auc
            roc_curve_plot = plot_roc_curve_from_cv_metrics(
                cv_result_metrics,
                plot_title=f"Classification of {target} using " f"{best_cv_estimator}",
            )
            roc_curve_plot_path = output_folder / (f"roc_auc_{plot_index}.png")
            roc_curve_plot.savefig(roc_curve_plot_path, dpi=300)
            plt.close(roc_curve_plot)

            # feature importance
            feature_importance = get_feature_importance(model)
            feature_importance_plot = plot_feature_importances(
                feature_importance, title=f"Feature importance for classification of \n {target} \n"
                                          f"using \n {type(classifiers[best_cv_estimator]).__name__}"
            )
            feature_importance_plot_path = output_folder / (
                f"feature_importance_{plot_index}.png"
            )
            feature_importance_csv_path = output_folder / (
                f"feature_importance_{plot_index}.csv"
            )
            feature_importance.to_csv(feature_importance_csv_path, sep=";")
            feature_importance_plot.savefig(feature_importance_plot_path, dpi=300)
            plt.close(feature_importance_plot)

            # save report
            selected_features = optimized_model["estimator"].feature_names_in_.tolist()
            negative_samples = (~df[target]).sum()
            positive_samples = (df[target]).sum()
            mean_auc_preds = cv_result_metrics["mean_auc_preds"]
            std_auc_preds = cv_result_metrics["std_auc_preds"]
            mean_auc_probs = cv_result_metrics["mean_auc_probs"]
            std_auc_probs = cv_result_metrics["std_auc_probs"]
            mean_f1 = cv_result_metrics["mean_f1"]
            std_f1 = cv_result_metrics["std_f1"]

            report_df.loc[len(report_df.index)] = update_report(
                target=target,
                features=selected_features,
                negative_samples=negative_samples,
                positive_samples=positive_samples,
                estimator_name=type(classifiers[best_cv_estimator]).__name__,
                mean_auc_preds=mean_auc_preds,
                std_auc_preds=std_auc_preds,
                mean_auc_probs=mean_auc_probs,
                std_auc_probs=std_auc_probs,
                mean_f1=mean_f1,
                std_f1=std_f1,
                roc_plot_path=roc_curve_plot_path,
                feature_importance_csv=feature_importance_csv_path,
                feature_importance_plot_path=feature_importance_plot_path,
                sampling=sample_method,
                best_params=best_params,
                feature_selection=feature_selection_method,
                selected_features=selected_features,
            )
            pbar.update(1)
            plot_index += 1
            report_df.to_excel(output_folder / "report.xlsx")
            report_df.to_csv(output_folder / "report.csv", sep=";")
        report_df.to_excel(output_folder / "report.xlsx")
        report_df.to_csv(output_folder / "report.csv", sep=";")
        return report_df


def single_shot_classification(
        df: pd.DataFrame,
        feature_cols: list[str],
        target_cols: list[str],
        sample_method: str,
        feature_selection_method: str,
        estimators: list[str],
        output_path: Path | str,
):
    # setup output folder
    output_path = Path(output_path)
    output_path.mkdir(exist_ok=True)
    output_folder = (
            output_path
            / f"gs_multivariate_analysis_{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}"
    )
    output_folder.mkdir(exist_ok=True)

    # get features and targets
    features, targets, feature_scale_levels = features_and_targets_from_dataframe(
        df, feature_cols, target_cols
    )
    if features.isnull().values.any():
        print("Features containing missing values. Using XGBClassifier to handle those.")
        estimators = ["xgboost"]
        feature_selection_method = None
        sample_method = None

    # iterate over targets and features
    report_df = make_report_df(sample_method, feature_selection_method)
    with tqdm(total=(targets.shape[1]) * len(estimators)) as pbar:
        plot_index = 0
        for target in targets:

            # train-test split
            y = df[target]
            X_train, X_test, y_train, y_test = train_test_split(features, y, stratify=y, test_size=0.2,
                                                                random_state=123)

            for estimator in estimators:
                estimator_name = type(classifiers[estimator]).__name__
                model = build_model(
                    feature_scale_levels,
                    sample_method,
                    feature_selection_method,
                    estimator,
                )
                classifier = model.fit(X_train, y_train)
                preds = model.predict(X_test)

                # f1 score
                f1 = f1_score(y_test, preds)
                # roc-auc
                lr_probs = classifier.predict_proba(X_test)
                lr_probs = lr_probs[:, 1]
                ns_probs = [0 for _ in range(len(y_test))]
                ns_auc = roc_auc_score(y_test, ns_probs)
                lr_auc_probs = roc_auc_score(y_test, lr_probs)
                lr_auc_preds = roc_auc_score(y_test, preds)
                ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)
                lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_probs)
                plt.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill ROC AUC=%.3f' % (ns_auc))
                plt.plot(lr_fpr, lr_tpr, marker='.', label='xgboost ROC AUC=%.3f' % (lr_auc_preds))
                plt.xlabel('False Positive Rate')
                plt.ylabel('True Positive Rate')
                plt.legend()
                roc_curve_plot_path = output_folder / (f"roc_auc_{plot_index}.png")
                plt.savefig(roc_curve_plot_path, format='pdf')

                # feature importance
                feature_importance = get_feature_importance(model)
                feature_importance_plot = plot_feature_importances(
                    feature_importance, title=f"Feature importance for classification of \n {target} \n"
                                              f"using \n {estimator_name}"
                )
                feature_importance_plot_path = output_folder / (
                    f"feature_importance_{plot_index}.png"
                )
                feature_importance_csv_path = output_folder / (
                    f"feature_importance_{plot_index}.csv"
                )
                feature_importance.to_csv(feature_importance_csv_path, sep=";")
                feature_importance_plot.savefig(feature_importance_plot_path, dpi=300)
                plt.close(feature_importance_plot)

                # save report
                selected_features = model["estimator"].feature_names_in_
                negative_samples = (~df[target]).sum()
                positive_samples = (df[target]).sum()
                mean_auc_probs = lr_auc_probs
                mean_auc_preds = lr_auc_preds
                std_auc_probs = "not applicable"
                std_auc_preds = "not applicable"
                mean_f1 = f1
                std_f1 = "not applicable"

                report_df.loc[len(report_df.index)] = update_report(
                    target=target,
                    features=selected_features,
                    negative_samples=negative_samples,
                    positive_samples=positive_samples,
                    estimator_name=estimator_name,
                    mean_auc_probs=mean_auc_probs,
                    mean_auc_preds=mean_auc_preds,
                    std_auc_preds=std_auc_preds,
                    std_auc_probs=std_auc_probs,
                    mean_f1=mean_f1,
                    std_f1=std_f1,
                    roc_plot_path=roc_curve_plot_path,
                    feature_importance_csv=feature_importance_csv_path,
                    feature_importance_plot_path=feature_importance_plot_path,
                    sampling=sample_method,
                    feature_selection=feature_selection_method,
                    selected_features=selected_features,
                )
                pbar.update(1)
                plot_index += 1
            report_df.to_excel(output_folder / "report.xlsx")
            report_df.to_csv(output_folder / "report.csv", sep=";")

        report_df.to_excel(output_folder / "report.xlsx")
        report_df.to_csv(output_folder / "report.csv", sep=";")
        return report_df


def univariate_classification(
        df: pd.DataFrame,
        feature_cols: list[str],
        target_cols: list[str],
        sample_method: str,
        estimators: list[str],
        output_path: Path | str,
):
    """
    Run a univariate classification pipeline with cross-validation and save the results.

    Args:
        df (pd.DataFrame): The input DataFrame containing features and targets.
        feature_cols (List[str]): List of column names containing features.
        target_cols (List[str]): List of column names containing target variables.
        sample_method (Optional[str]): The method for addressing class imbalance, if any.
        estimators (List[str]): List of classifier names to use in the pipeline.
        output_path (Optional[Path]): Path to the output folder. Defaults to 'output'.

    Returns:
        pd.DataFrame: A DataFrame containing the results of the classification.

    Raises:
        Any specific exceptions or errors.

    Example:
        >>> result_df = multivariate_classification(
        ...     df=data_frame,
        ...     feature_cols=['feature1', 'feature2'],
        ...     target_cols=['target'],
        ...     sample_method='smote',
        ...     estimators=['random_forest', 'logistic_regression'],
        ...     output_path=Path('results'),
        ... )

    Note:
        - The function runs a univariate classification pipeline for each target column and each specified estimator.
        - Cross-validation is performed, and results including ROC-AUC and feature importance are saved.
        - The output is stored in the specified output_path.
    """
    feature_selection_method = None  # redundant for univariate analysis
    with tqdm(total=(len(target_cols) * len(feature_cols) * len(estimators))) as pbar:
        # setup output folder
        output_path = Path(output_path)
        output_path.mkdir(exist_ok=True)
        output_folder = (
                output_path
                / f"univariate_analysis_{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}"
        )
        output_folder.mkdir(exist_ok=True)

        report_df = make_report_df(sample_method, feature_selection_method)
        # iterate over feaures
        plot_index = 0
        for feature in feature_cols:
            feature_cols_ = [feature]

            # get features and targets
            (
                features,
                targets,
                feature_scale_levels,
            ) = features_and_targets_from_dataframe(df, feature_cols_, target_cols)

            if feature_scale_levels["categorical"]:
                feature_cols_ = features.columns.tolist()
            if features.isnull().values.any():
                print("Features containing missing values. Using XGBClassifier to handle those.")
                estimators = ["xgboost"]

            # iterate over targets
            for target in targets:
                for estimator in estimators:
                    estimator_name = type(classifiers[estimator]).__name__
                    model = build_model(
                        feature_scale_levels,
                        sample_method,
                        feature_selection_method,
                        estimator,
                    )
                    cv_result = cross_validate_model(model, features, df[target])
                    cv_result_metrics = metrics_from_cv_result(cv_result)

                    # roc-auc
                    roc_curve_plot = plot_roc_curve_from_cv_metrics(
                        cv_result_metrics,
                        plot_title=f"Classification of {target} using "
                                   f"{estimator_name}",
                    )
                    roc_curve_plot_path = output_folder / (f"roc_auc_{plot_index}.png")
                    roc_curve_plot.savefig(roc_curve_plot_path, dpi=600)
                    plt.close(roc_curve_plot)

                    # feature importance
                    feature_importance = get_feature_importance(model)
                    feature_importance_plot = plot_feature_importances(
                        feature_importance
                    )
                    feature_importance_plot_path = output_folder / (
                        f"feature_importance_{plot_index}.png"
                    )
                    feature_importance_csv_path = output_folder / (
                        f"feature_importance_{plot_index}.csv"
                    )
                    feature_importance.to_csv(feature_importance_csv_path, sep=";")
                    feature_importance_plot.savefig(
                        feature_importance_plot_path, dpi=300
                    )
                    plt.close(feature_importance_plot)

                    # save report
                    features_in = model["estimator"].feature_names_in_.tolist()
                    negative_samples = (~df[target]).sum()
                    positive_samples = (df[target]).sum()
                    mean_auc_preds = cv_result_metrics["mean_auc_preds"]
                    std_auc_preds = cv_result_metrics["std_auc_preds"]
                    mean_auc_probs = cv_result_metrics["mean_auc_probs"]
                    std_auc_probs = cv_result_metrics["std_auc_probs"]
                    mean_f1 = cv_result_metrics["mean_f1"]
                    std_f1 = cv_result_metrics["std_f1"]

                    report_df.loc[len(report_df.index)] = update_report(
                        target=target,
                        features=features_in,
                        negative_samples=negative_samples,
                        positive_samples=positive_samples,
                        estimator_name=estimator_name,
                        mean_auc_preds=mean_auc_preds,
                        std_auc_preds=std_auc_preds,
                        mean_auc_probs=mean_auc_probs,
                        std_auc_probs=std_auc_probs,
                        mean_f1=mean_f1,
                        std_f1=std_f1,
                        roc_plot_path=roc_curve_plot_path,
                        feature_importance_csv=feature_importance_csv_path,
                        feature_importance_plot_path=feature_importance_plot_path,
                        sampling=sample_method,
                    )
                    pbar.update(1)
                    plot_index += 1
                report_df.to_excel(output_folder / "report.xlsx")
                report_df.to_csv(output_folder / "report.csv", sep=";")

            report_df.to_excel(output_folder / "report.xlsx")
            report_df.to_csv(output_folder / "report.csv", sep=";")
        return report_df
