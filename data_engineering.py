from cryptocompare.blockchain_data import get_blockchain_data
from cryptocompare.ohlcv import get_ohlcv
import pandas as pd
from ta.momentum import RSIIndicator, WilliamsRIndicator, UltimateOscillator
from ta.trend import SMAIndicator, EMAIndicator, MACD
from ta.volatility import BollingerBands
from ta.volume import OnBalanceVolumeIndicator
from ta.volume import AccDistIndexIndicator

def build_features_TA(ohlcv_data, fsyms):
    features = pd.DataFrame(ohlcv_data[['symbol', 'date']])

    for fsym in fsyms:
        sma_5 = SMAIndicator(close=ohlcv_data[ohlcv_data['symbol'] == fsym]['close'], window=5)
        sma_30 = SMAIndicator(close=ohlcv_data[ohlcv_data['symbol'] == fsym]['close'], window=30)
        sma_60 = SMAIndicator(close=ohlcv_data[ohlcv_data['symbol'] == fsym]['close'], window=60)

        ema_5 = EMAIndicator(close=ohlcv_data[ohlcv_data['symbol'] == fsym]['close'], window=5)
        ema_30 = EMAIndicator(close=ohlcv_data[ohlcv_data['symbol'] == fsym]['close'], window=30)
        ema_60 = EMAIndicator(close=ohlcv_data[ohlcv_data['symbol'] == fsym]['close'], window=60)	

        macd = MACD(
            ohlcv_data[ohlcv_data['symbol'] == fsym]['close'],
            window_slow=26, 
            window_fast=12, 
            window_sign=9
        )

        rsi = RSIIndicator(
            ohlcv_data[ohlcv_data['symbol'] == fsym]['close'],
            window=14)
        

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

        features.loc[features['symbol'] == fsym, 'sma_5'] = sma_5.sma_indicator()
        features.loc[features['symbol'] == fsym, 'sma_30'] = sma_30.sma_indicator()
        features.loc[features['symbol'] == fsym, 'sma_60'] = sma_60.sma_indicator()

        features.loc[features['symbol'] == fsym, 'ema_5'] = ema_5.ema_indicator()
        features.loc[features['symbol'] == fsym, 'ema_30'] = ema_30.ema_indicator()
        features.loc[features['symbol'] == fsym, 'ema_60'] = ema_60.ema_indicator()

        features.loc[features['symbol'] == fsym, 'rsi'] = rsi.rsi()
        features.loc[features['symbol'] == fsym, 'macd_diff'] = macd.macd_diff()

        features.loc[features['symbol'] == fsym, 'OBV'] = obv.on_balance_volume()
        features.loc[features['symbol'] == fsym, 'ADI'] = adi.acc_dist_index()
        features.loc[features['symbol'] == fsym, 'WILLR'] = willr.williams_r()

        features.loc[features['symbol'] == fsym, 'ULTOSC'] = ult_osc.ultimate_oscillator()

    return features


def build_target(ohlcv_data, fsyms):
    # Create outcomes DataFrame
    outcomes = pd.DataFrame(ohlcv_data[['symbol', 'date']])

    for fsym in fsyms:
        outcomes.loc[outcomes['symbol'] == fsym, 'close_1'] = ohlcv_data[ohlcv_data['symbol'] == fsym]['close'].pct_change(-1)
        outcomes.loc[outcomes['symbol'] == fsym, 'close_3'] = ohlcv_data[ohlcv_data['symbol'] == fsym]['close'].pct_change(-3)
        outcomes.loc[outcomes['symbol'] == fsym, 'close_5'] = ohlcv_data[ohlcv_data['symbol'] == fsym]['close'].pct_change(-5)
        outcomes.loc[outcomes['symbol'] == fsym, 'close_7'] = ohlcv_data[ohlcv_data['symbol'] == fsym]['close'].pct_change(-7)

        outcomes.loc[outcomes['symbol'] == fsym, 'direction_1'] = outcomes.loc[outcomes['symbol'] == fsym, 'close_1'].apply(lambda x: 1 if x > 0 else 0)
        outcomes.loc[outcomes['symbol'] == fsym, 'direction_3'] = outcomes.loc[outcomes['symbol'] == fsym, 'close_3'].apply(lambda x: 1 if x > 0 else 0)
        outcomes.loc[outcomes['symbol'] == fsym, 'direction_5'] = outcomes.loc[outcomes['symbol'] == fsym, 'close_5'].apply(lambda x: 1 if x > 0 else 0)
        outcomes.loc[outcomes['symbol'] == fsym, 'direction_7'] = outcomes.loc[outcomes['symbol'] == fsym, 'close_7'].apply(lambda x: 1 if x > 0 else 0)
    
    return outcomes