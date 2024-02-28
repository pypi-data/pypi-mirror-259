import numpy as np
import lime.lime_tabular
import shap

# 02 Define preprocess data function and explainer
class preprocess:
    def _preprocess_data(df, feature_names, target_name, point_index, weights):
        weight = weights[point_index]
        X_weighted = df[feature_names].multiply(weight, axis=0)
        y_weighted = df[target_name] * weight
        non_zero_indices = np.nonzero(weight)[0]
        selected_points = non_zero_indices[non_zero_indices != point_index]
        X_train = X_weighted.iloc[selected_points].values
        y_train = y_weighted.iloc[selected_points]
        current_point = X_weighted.iloc[point_index].values.reshape(1, -1)
        return X_train, y_train, current_point

    def _calculate_lime_importances(model, X_train, X_test, feature_names, target_name):
        explainer = lime.lime_tabular.LimeTabularExplainer(
            training_data=X_train,
            feature_names=feature_names,
            class_names=[target_name],
            mode='regression',
            discretize_continuous=False,
        )
        exp = explainer.explain_instance(data_row=X_test[0], predict_fn=model.predict)
        lime_importances_dict = dict(exp.as_list())
        importances = np.array([lime_importances_dict.get(feature, 0) for feature in feature_names])
        return importances

    def _calculate_shap_importances(model, X_train, X_test):
        explainer = shap.Explainer(model, X_train)
        shap_values = explainer(X_test)
        return np.abs(shap_values.values).mean(axis=0)