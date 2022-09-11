import cryptocompare
import datetime
import pandas as pd
from config import API_KEY



def get_historical_price_minute():

    cryptocompare.cryptocompare._set_api_key_parameter(f'{API_KEY}')

    historical_price_minute = cryptocompare.get_historical_price_minute('ETH', currency='USD', limit=2000)
    df = pd.DataFrame(historical_price_minute)
    min_timestamp = df['time'].min()

    for i in range(0, 5):
        historical_price_minute = cryptocompare.get_historical_price_minute('ETH', currency='USD', limit=2000, toTs=min_timestamp)
        df_temp = pd.DataFrame(historical_price_minute)
        min_timestamp = df_temp['time'].min()
        df = pd.concat([df, df_temp])

    df['date'] = df['time'].apply(lambda x: datetime.datetime.fromtimestamp(x))
    df = df.sort_values(by='date')
    df = df.reset_index()
    return df

df = get_historical_price_minute()

df.to_csv('data/historical_price_minute.csv')

print(df)