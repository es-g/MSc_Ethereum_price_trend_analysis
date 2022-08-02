import datetime
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

now = datetime.datetime.now()
now_str = now.strftime("%Y%m%dT%H%M%S")

def fit_expanding_window(features, outcome, model_instance, scaling=True):
    """Train models using Expanding Window technique

    Args:
        features (_type_): _description_
        outcome (_type_): _description_
        model (_type_): _description_
        scaling (bool, optional): _description_. Defaults to True.

    Returns:
        _type_: _description_
    """    
   
    recalc_dates = features.resample('M').mean().index[:-1]

    

    models_expanding_window = pd.Series(index=recalc_dates, dtype='float')

    with open('logging/{ts}.log'.format(ts=now_str), 'w') as f:
        for i, date in enumerate(recalc_dates):
            minmax_scaler = MinMaxScaler()
            X_train = features.loc[:date, :]
            y_train = outcome.loc[:date]
            
            X_train_scaled = minmax_scaler.fit_transform(X_train)
            model = model_instance

            if scaling:
                model.fit(X_train_scaled, y_train)
            else:
                model.fit(X_train, y_train)
            f.write("Training on the first {} records, from {} to {}\n".
                format(len(y_train), y_train.index.min(), y_train.index.max()))

            
            models_expanding_window.loc[date] = model

    return models_expanding_window


def predict_expanding_window(models_expanding_window, features, scaling=True):
    """Predict the values using expanding window technique 

    Args:
        models_expanding_window (_type_): _description_
        features (_type_): _description_

    Returns:
        _type_: _description_
    """    

    recalc_dates = features.resample('M').mean().index[:-1]
    models = pd.Series(index=recalc_dates, dtype='object')

    begin_dates = models.index
    end_dates = models.index[1:].append(pd.to_datetime(['2099-12-31']))
    predictions_expanding_window = pd.Series(index=features.index, dtype='float')

    minmax_scaler = MinMaxScaler()

    for i, model in enumerate(models_expanding_window):
        X = features.loc[begin_dates[i]:end_dates[i]]
        X_scaled = minmax_scaler.fit_transform(X)
        
        if scaling:
            p = pd.Series(model.predict(X_scaled), index=X.index, dtype='float')
        else:
            p = pd.Series(model.predict(X), index=X.index, dtype='float')

        print('Predicting for the period between {begin_dates} and {end_dates}\n'.format(
            begin_dates=begin_dates[i], end_dates=end_dates[i])
            )

        predictions_expanding_window.loc[X.index] = p

    return predictions_expanding_window


def fit_rolling_window(features, outcome, model_instance, scaling=True):
    
    recalc_dates = features.resample('M').mean().index[:-1]
    models_rolling_window = pd.Series(index=recalc_dates, dtype='float')

    minmax_scaler = MinMaxScaler()

    for date in recalc_dates:
        X_train = features.loc[date-pd.Timedelta('30 days'):date, :]
        y_train = outcome.loc[date-pd.Timedelta('30 days'):date]
        
        X_train_scaled = minmax_scaler.fit_transform(X_train)

        model = model_instance

        if scaling:
            model.fit(X_train_scaled, y_train)
        else:
            model.fit(X_train, y_train)

        print("Training on the most recent {} records, from {} to {}\n".
            format(len(y_train), y_train.index.min(), y_train.index.max()))

        models_rolling_window.loc[date] = model

    return models_rolling_window


def predict_rolling_window(models_rolling_window, features, scaling=True):

    predictions_rolling_window = pd.Series(index=features.index, dtype='float')
    begin_dates = models_rolling_window.index
    end_dates = models_rolling_window.index[1:].append(pd.to_datetime(['2099-12-31']))
    minmax_scaler = MinMaxScaler()

    for i, model in enumerate(models_rolling_window):
        X = features.loc[begin_dates[i]:end_dates[i]]
        X_scaled = minmax_scaler.fit_transform(X)
        if scaling:
            p = pd.Series(model.predict(X_scaled), index=X.index, dtype='float')
        else:
            p = pd.Series(model.predict(X), index=X.index, dtype='float')

        print('Predicting for the prediod between {} and {}\n'.format(X.index.min(), X.index.max()))
        predictions_rolling_window.loc[X.index] = p

    return predictions_rolling_window
    


def train_and_predict_expanding(features, outcome, model_instance, scaling=True):
    
    recalc_dates = features.resample('M').mean().index[:-1]

    models_expanding_window = pd.Series(index=recalc_dates, dtype='float')

    begin_dates = models_expanding_window.index
    end_dates = models_expanding_window.index[1:].append(pd.to_datetime(['2099-12-31']))
    predictions_expanding_window = pd.Series(index=features.index, dtype='float')

    with open('logging/{ts}.log'.format(ts=now_str), 'w') as f:
        for i, date in enumerate(recalc_dates):
            minmax_scaler = MinMaxScaler()
            X_train = features.loc[:date, :]
            y_train = outcome.loc[:date]
            
            model = model_instance

            if scaling:
                X_train_scaled = minmax_scaler.fit_transform(X_train)
                model.fit(X_train_scaled, y_train)
            else:
                model.fit(X_train, y_train)
            f.write("Training on the first {} records, from {} to {}\n".
                format(len(y_train), y_train.index.min(), y_train.index.max()))
            # models_expanding_window.loc[date] = model


            # Running inference
            X_test = features.loc[begin_dates[i]:end_dates[i]]
            
            if scaling:
                X_test_scaled = minmax_scaler.fit_transform(X_test)
                p = pd.Series(model.predict(X_test_scaled), index=X_test.index, dtype='float')
            else:
                p = pd.Series(model.predict(X_test), index=X_test.index, dtype='float')

            f.write('Predicting for the period between {begin_dates} and {end_dates}\n'.format(
                begin_dates=begin_dates[i], end_dates=end_dates[i])
                )

            predictions_expanding_window.loc[X_test.index] = p


    return predictions_expanding_window