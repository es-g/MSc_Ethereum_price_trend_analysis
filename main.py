import pandas as pd
import blockchain_and_prices


ohlcv_data = blockchain_and_prices.get_price_data('ETH')

df = ohlcv_data['close'] / ohlcv_data['open'] - 1
outcomes = pd.DataFrame(index=ohlcv_data.index)

# Next day's return
outcomes['close_1'] = ohlcv_data['close'].pct_change(-1)

# Return in 5 days
outcomes['close_5'] = ohlcv_data['close'].pct_change(-5)

# Return in 10 days
outcomes['close_10'] = ohlcv_data['close'].pct_change(-10)
