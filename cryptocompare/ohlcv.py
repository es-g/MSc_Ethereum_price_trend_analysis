import datetime
import pandas as pd
import matplotlib.pyplot as plt
import requests


headers = {'authorization': 'Apikey c8642fe0530de2b383434ac6889280d5468ece6a5c89fea8aab6ef73ea06620e'}

endpoints = {
    'blockchain': 'https://min-api.cryptocompare.com/data/blockchain/histo/day',
    'daily_symbol_vol' :'https://min-api.cryptocompare.com/data/symbol/histoday',
    'ohlcv': 'https://min-api.cryptocompare.com/data/v2/histoday'
}


def get_ohlcv(fsym):    
    """Iterates through data given the API limit to get prices data

    Args:
        fsym (str): Cryptocurrency
 
    """    
    yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
    toTs = datetime.datetime.timestamp(yesterday)
    count = 0
    next_page = True

    # Initialize pandas DataFrame object
    df = pd.DataFrame()
    print('---- Extracting price data for {} ... ---- \n'.format(fsym))

    while(next_page):
        count += 1
        print('Run number: {count} \n'.format(count=count))

        url = '{endpoint}?fsym={fsym}&limit=2000&toTs={toTs}&tsym=USD'.format(fsym=fsym, toTs=toTs, endpoint=endpoints['ohlcv'])

        r = requests.get(url, headers=headers)

        if r.json()['Response'] == 'Success':
            print('Response received')
            toTs = r.json()['Data']['TimeFrom']

            from_date = datetime.datetime.fromtimestamp(r.json()['Data']['TimeFrom'])
            to_date = datetime.datetime.fromtimestamp(r.json()['Data']['TimeTo'])

            print('Date range: From {from_date} To {to_date}'.format(from_date=from_date, to_date=to_date))
            
            if not r.json()['Data']['Data'][0].get('high'):
                print('No more data received. Terminating the loop at run {count} \n'.format(count=count))
                next_page = False

            # Append to the end of the DataFrame
            df = pd.concat([df, pd.json_normalize(r.json()['Data']['Data'])])

    df['date'] = df['time'].apply(lambda x: datetime.datetime.fromtimestamp(x))
    df = df.sort_values(by='date')

    # Remove zero values
    df = df[df['high'] != 0]
    df = df.reset_index()

    return df