import pandas as pd
from TimeBasedCV import TimeBasedCV
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, f1_score, confusion_matrix, recall_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.svm import SVC


def fit_predict(model_instance, X, y, train_period=60, test_period=14):

    tscv = TimeBasedCV(train_period=train_period, test_period=test_period)

    split_indices = tscv.split(X, gap=1)

    test_data_indices = [item[1] for item in split_indices]
    test_data_indices = [item for sublist in test_data_indices for item in sublist]

    preds = pd.Series(index=X.loc[test_data_indices]['date'], dtype='object')

    for train_index, test_index in split_indices:
        scaler = MinMaxScaler()
        test_dates = X.loc[test_index]['date']
        X_train = X.loc[train_index].drop('date', axis=1)
        X_train = scaler.fit_transform(X_train)
        y_train = y.loc[train_index]

        X_test = X.loc[test_index].drop('date', axis=1)
        X_test = scaler.fit_transform(X_test)

        clf = model_instance
        clf.fit(X_train, y_train)
        y_train_pred = clf.predict(X_train)

        # print(y_train_pred)
        

        accuracy = accuracy_score(y_true=y_train, y_pred=list(y_train_pred)),

        preds[test_dates] = clf.predict(X_test)


    return preds, accuracy


def evaluate_model(y_true, y_pred):
    metrics = {}

    metrics['accuracy'] = accuracy_score(y_true=y_true, y_pred=y_pred)
    metrics['precision'] = precision_score(y_true=y_true, y_pred=y_pred)
    metrics['f1_score'] = f1_score(y_true=y_true, y_pred=y_pred)
    metrics['recall'] = recall_score(y_true=y_true, y_pred=y_pred)

    return metrics


def get_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true=y_true, y_pred=y_pred)

    return cm