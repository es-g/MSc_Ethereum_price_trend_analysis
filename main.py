import blockchain_and_prices as bp
import pandas as pd
import ta
from ta.volatility import AverageTrueRange
from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.volatility import BollingerBands
from ta.volume import OnBalanceVolumeIndicator
from technical_indicators import bollinger_bands
from ta.volume import AccDistIndexIndicator

fsyms = ['ETH', 'BTC', 'DOGE', 'MATIC']

# Collect data
ohlcv_data = pd.DataFrame()
blockchain_data = pd.DataFrame()

for fsym in fsyms:
    ohlcv_data_temp = bp.get_price_data(fsym)
    ohlcv_data_temp['symbol'] = fsym
    ohlcv_data = pd.concat([ohlcv_data, ohlcv_data_temp])

    blockchain_data_temp = bp.get_blockchain_data(fsym)
    blockchain_data = pd.concat([blockchain_data, blockchain_data_temp])

ohlcv_data = ohlcv_data.reset_index().drop(columns=['index'])

# Feature Engineering
features = pd.DataFrame(ohlcv_data[['symbol', 'date']])

for fsym in fsyms:
	rsi = RSIIndicator(
		ohlcv_data[ohlcv_data['symbol'] == fsym]['close'],
		window=14
	)

	macd = MACD(
		ohlcv_data[ohlcv_data['symbol'] == fsym]['close']
	)

	bollinger_bands = BollingerBands(
		ohlcv_data[ohlcv_data['symbol'] == fsym]['close']
	)

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

	features.loc[features['symbol'] == fsym, 'rsi'] = rsi.rsi()
	features.loc[features['symbol'] == fsym, 'macd_line'] = macd.macd()
	features.loc[features['symbol'] == fsym, 'macd_signal'] = macd.macd_signal()
	features.loc[features['symbol'] == fsym, 'macd_histogram'] = macd.macd_diff()
	features.loc[features['symbol'] == fsym, 'mavg'] = bollinger_bands.bollinger_mavg()
	features.loc[features['symbol'] == fsym, 'bollinger_hband'] = bollinger_bands.bollinger_hband()
	features.loc[features['symbol'] == fsym, 'bollinger_lband'] = bollinger_bands.bollinger_lband()
	features.loc[features['symbol'] == fsym, 'OBV'] = obv.on_balance_volume()
	features.loc[features['symbol'] == fsym, 'ADI'] = adi.acc_dist_index()

# Create outcomes DataFrame
outcomes = pd.DataFrame()

outcomes['close_1'] = ohlcv_data[ohlcv_data['symbol'] == 'ETH']['close'].pct_change(1)
outcomes['close_5'] = ohlcv_data[ohlcv_data['symbol'] == 'ETH']['close'].pct_change(5)
outcomes['close_10'] = ohlcv_data[ohlcv_data['symbol'] == 'ETH']['close'].pct_change(10)
