from sklearn.model_selection import RandomizedSearchCV


def find_best_params(estimator, params, split_indices, features, outcomes):
    model = RandomizedSearchCV(
        estimator = estimator,
        param_distributions = params,
        n_iter = 10,
        n_jobs = -1,
        cv = split_indices,
        verbose=5,
        pre_dispatch='2*n_jobs',
        random_state = None,
        return_train_score = True)

    model.fit(features.drop('date', axis=1), outcomes)

    best_params = model.best_params_

    return best_params
