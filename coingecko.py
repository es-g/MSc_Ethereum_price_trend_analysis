from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

coins_markets = cg.get_coins_markets('BTC')

print(cg)