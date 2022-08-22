import cryptocompare
import datetime
import pandas as pd



def get_historical_price_minute():

    cryptocompare.cryptocompare._set_api_key_parameter('c8642fe0530de2b383434ac6889280d5468ece6a5c89fea8aab6ef73ea06620e')

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