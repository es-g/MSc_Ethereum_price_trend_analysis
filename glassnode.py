import json
import requests
import pandas as pd


# insert your API key here
API_KEY = '2AoV3hU5kI9N2MvTJ5N5tFtwX4q'


fsyms = ['ETH', 'BTC']

server_name = 'https://api.glassnode.com/v1/metrics'
endpoints = {
    'price_usd_ohlc': '/market/price_usd_ohlc',
    'market_cap': '/market/marketcap_usd',
    'circulating_supply': '/supply/current'
}

# make API request
res = requests.get(server_name+endpoints['circulating_supply'],
    params={'a': 'BTC', 'api_key': API_KEY})

res2 = requests.get(server_name+endpoints['price_usd_ohlc'],
    params={'a': 'BTC', 'api_key': API_KEY})


# convert to pandas dataframe
df_glassnode = pd.read_json(res.text, convert_dates=['t'])
df_glassnode2 = pd.read_json(res2.text, convert_dates=['t'])

print(df_glassnode.head())