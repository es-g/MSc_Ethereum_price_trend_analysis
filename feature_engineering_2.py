from cryptocompare_files.blockchain_data import get_blockchain_data
from cryptocompare_files.ohlcv import get_ohlcv
import pandas as pd
from ta.momentum import RSIIndicator, WilliamsRIndicator, UltimateOscillator
from ta.trend import SMAIndicator, EMAIndicator, MACD
from ta.volume import OnBalanceVolumeIndicator
from ta.volume import AccDistIndexIndicator


def build_features_TA(ohlcv_data, fsyms):
    features = pd.DataFrame(ohlcv_data[['symbol', 'date']])

    for fsym in fsyms:
        for window in range(5, 60):
            # Simple Moving Average
            sma = SMAIndicator(close=ohlcv_data[ohlcv_data['symbol'] == fsym]['close'], window=window)            
            features.loc[features['symbol'] == fsym,
                        f'sma_{window}'] = sma.sma_indicator()

            # Exponential Moving Average
            ema = EMAIndicator(close=ohlcv_data[ohlcv_data['symbol'] == fsym]['close'], window=window)
                   
            features.loc[features['symbol'] == fsym,
                        f'ema_{window}'] = ema.ema_indicator()
        


        macd = MACD(
            ohlcv_data[ohlcv_data['symbol'] == fsym]['close'],
            window_slow=26,
            window_fast=12,
            window_sign=9
        )

        rsi_5 = RSIIndicator(
            ohlcv_data[ohlcv_data['symbol'] == fsym]['close'],
            window=5)

        rsi_10 = RSIIndicator(
            ohlcv_data[ohlcv_data['symbol'] == fsym]['close'],
            window=10)

        rsi_30 = RSIIndicator(
            ohlcv_data[ohlcv_data['symbol'] == fsym]['close'],
            window=30)

        rsi_60 = RSIIndicator(
            ohlcv_data[ohlcv_data['symbol'] == fsym]['close'],
            window=60)

        obv = OnBalanceVolumeIndicator(
            ohlcv_data[ohlcv_data['symbol'] == fsym]['close'],
            ohlcv_data[ohlcv_data['symbol'] == fsym]['volumefrom']
        )

        adi = AccDistIndexIndicator(
            ohlcv_data[ohlcv_data['symbol'] == fsym]['high'],
            ohlcv_data[ohlcv_data['symbol'] == fsym]['low'],
            ohlcv_data[ohlcv_data['symbol'] == fsym]['close'],
            ohlcv_data[ohlcv_data['symbol'] == fsym]['volumefrom']
        )

        willr = WilliamsRIndicator(
            high=ohlcv_data[ohlcv_data['symbol'] == fsym]['high'],
            low=ohlcv_data[ohlcv_data['symbol'] == fsym]['low'],
            close=ohlcv_data[ohlcv_data['symbol'] == fsym]['close'],
            lbp=14
        )

        ult_osc = UltimateOscillator(
            high=ohlcv_data[ohlcv_data['symbol'] == fsym]['high'],
            low=ohlcv_data[ohlcv_data['symbol'] == fsym]['low'],
            close=ohlcv_data[ohlcv_data['symbol'] == fsym]['close'],
            window1=7,
            window2=14,
            window3=28
        )

        # Calculating TA indicators

        for window in range(5, 60):
            features.loc[features['symbol'] == fsym, 'return_{window}'.format(
                window=window)] = ohlcv_data[ohlcv_data['symbol'] == fsym]['close'].pct_change(window)
            features.loc[features['symbol'] == fsym, 'close_sma_{window}'.format(
                window=window)] = ohlcv_data[ohlcv_data['symbol'] == fsym]['close'] / features.loc[features['symbol'] == fsym, 'sma_{window}'.format(window=window)]
            features.loc[features['symbol'] == fsym, 'close_ema_{window}'.format(
                window=window)] = ohlcv_data[ohlcv_data['symbol'] == fsym]['close'] / features.loc[features['symbol'] == fsym, 'ema_{window}'.format(window=window)]

            features.loc[features['symbol'] == fsym, 'close-sma_{window}'.format(
                window=window)] = ohlcv_data[ohlcv_data['symbol'] == fsym]['close'] - features.loc[features['symbol'] == fsym, 'sma_{window}'.format(window=window)]    
            features.loc[features['symbol'] == fsym, 'close-ema_{window}'.format(
                window=window)] = ohlcv_data[ohlcv_data['symbol'] == fsym]['close'] - features.loc[features['symbol'] == fsym, 'ema_{window}'.format(window=window)]    

        features.loc[features['symbol'] == fsym, 'rsi_5'] = rsi_5.rsi()
        features.loc[features['symbol'] == fsym, 'rsi_10'] = rsi_10.rsi()
        features.loc[features['symbol'] == fsym, 'rsi_30'] = rsi_30.rsi()
        features.loc[features['symbol'] == fsym, 'rsi_60'] = rsi_60.rsi()

        features.loc[features['symbol'] == fsym,
                     'macd_diff'] = macd.macd_diff()

        features.loc[features['symbol'] == fsym,
                     'OBV'] = obv.on_balance_volume()
        
        features.loc[features['symbol'] == fsym, 'ADI'] = adi.acc_dist_index()
        features.loc[features['symbol'] == fsym, 'WILLR'] = willr.williams_r()

        features.loc[features['symbol'] == fsym,
                     'ULTOSC'] = ult_osc.ultimate_oscillator()
        
        for i in range(1, 30):
            features.loc[features['symbol'] == fsym,
                        f'OBV_pct_change_{i}'] = features.loc[features['symbol'] == fsym, 'OBV'].pct_change(i)
            features.loc[features['symbol'] == fsym,
                        f'OBV_diff_{i}'] = features.loc[features['symbol'] == fsym, 'OBV'].diff(i)

        features.loc[features['symbol'] == fsym,
                     'ADI_pct_change_1'] = features.loc[features['symbol'] == fsym, 'ADI'].pct_change()
        features.loc[features['symbol'] == fsym,
                     'ADI_diff_1'] = features.loc[features['symbol'] == fsym, 'ADI'].diff()

        # features = features.drop(columns=[
        #                          'sma_5', 'sma_10', 'sma_30', 'sma_60', 'ema_5', 'ema_10', 'ema_30', 'ema_60', 'OBV', 'ADI'])

    return features


def build_target(ohlcv_data, fsyms):
    # Create outcomes DataFrame
    outcomes = pd.DataFrame(ohlcv_data[['symbol', 'date']])

    for fsym in fsyms:
        for i in range(1, 8):
            outcomes.loc[outcomes['symbol'] == fsym,
                         f'close_{i}'] = ohlcv_data[ohlcv_data['symbol'] == fsym]['close'].pct_change(-i)
            outcomes.loc[outcomes['symbol'] == fsym, f'direction_{i}'] = outcomes.loc[outcomes['symbol']
                                                                                      == fsym, f'close_{i}'].apply(lambda x: 1 if x > 0 else 0)

    return outcomes
