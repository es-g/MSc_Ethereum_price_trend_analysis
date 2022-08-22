
from datetime import datetime
from pytrends.request import TrendReq

pytrend = TrendReq()

kw_list = ['ethereum','ETH']
start_period = datetime(2022, 8, 6)
now = datetime.now()

def get_historical_interest(kw_list, start, now):
    historical_interest = pytrend.get_historical_interest(
        kw_list, 
        year_start=start.year,
        month_start=start.month, 
        day_start=start.day, 
        hour_start=0, 
        year_end=now.year, 
        month_end=now.month, 
        day_end=now.day, 
        hour_end=now.hour, 
        cat=0, 
        sleep=0.5)

    return historical_interest

historical_interest = get_historical_interest(kw_list, start_period, now)
print('Successfully extracted Google Trends data')

historical_interest.to_csv('data/new.csv')
print('Successfully wrote into CSV file')
