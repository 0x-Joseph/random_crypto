from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

stables = ["usdc", "usdt", "ust", "usd"]

print(cg.get_price(ids='bitcoin', vs_currencies=stables))
print(cg.get_supported_vs_currencies())
# print(cg.ping())