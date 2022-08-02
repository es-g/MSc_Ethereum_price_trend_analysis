import cryptocompare
from matplotlib.pyplot import hist

cryptocompare.cryptocompare._set_api_key_parameter('c8642fe0530de2b383434ac6889280d5468ece6a5c89fea8aab6ef73ea06620e')

historical_price_minute = cryptocompare.get_historical_price_minute('BTC', currency='USD', limit=2000)

print(historical_price_minute)