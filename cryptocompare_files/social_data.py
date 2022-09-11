import datetime
import pandas as pd
import requests
from config import API_KEY



headers = {'authorization': 'Apikey {API_KEY}'.format(API_KEY)}

def get_social_data(coinId):    
    """NOT COMPLETE
    TO BE DONE
    """    
    yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
    toTs = datetime.datetime.timestamp(yesterday)
    count = 0
    next_page = True

    # Initialize pandas DataFrame object
    df = pd.DataFrame()
    print('---- Extracting price data for Coin ID{} ... ---- \n'.format(coinId))

    while(next_page):
        count += 1
        print('Run number: {count} \n'.format(count=count))

        url = 'https://min-api.cryptocompare.com/data/social/coin/histo/day?coinId={coinId}&limit=2000&toTs={toTs}&tsym=USD'.format(coundId=coinId, toTs=toTs)

        r = requests.get(url, headers=headers)

        if r.json()['Response'] == 'Success':
            print('Response received')
            toTs = r.json()['Data']['TimeFrom']

            from_date = datetime.datetime.fromtimestamp(r.json()['Data']['TimeFrom'])
            to_date = datetime.datetime.fromtimestamp(r.json()['Data']['TimeTo'])

            print('Date range: From {from_date} To {to_date}'.format(from_date=from_date, to_date=to_date))
            
            if not r.json()['Data'][0].get('overview_page_views'):
                print('No more data received. Terminating the loop at run {count} \n'.format(count=count))
                next_page = False

            # Append to the end of the DataFrame
            df = pd.concat([df, pd.json_normalize(r.json()['Data'])])

    df['date'] = df['time'].apply(lambda x: datetime.datetime.fromtimestamp(x))
    df = df.sort_values(by='date')

    # Remove zero values
    df = df[df['high'] != 0]
    df = df.reset_index()

    return df