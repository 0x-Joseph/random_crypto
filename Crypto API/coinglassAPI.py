# Crypto Derivatives data extraction via API @ https://open-api.coinglass.com

from code import interact
import json
import requests

symbol = 'BTC'
# key = "efd2f30a7fbc42d3a63be3f698fc370a"
# url = "http://open-api.coinglass.com/api/pro/v1/futures/openInterest?interval={interval}&symbol={symbol}"
url = "http://open-api.coinglass.com/api/pro/v1/option/openInterest?symbol={symbol}&coinglassSecret={coinglassSecret}"
params = {
}
# interval = '1hr'

# params = {
    # 'interval' : 0
    # }
# params = {
#     'interval' : '1hr',
#     'symbol' = 'BTC'
#     }
headers = {
    'coinglassSecret' : 'efd2f30a7fbc42d3a63be3f698fc370a'
}
response = requests.request("GET", url, headers=headers, data = params)
# print(response.text.encode('utf8'))

result = requests.get(url, headers=headers, data=params)
print(json(result))
# curl --location --request GET 'http://open-api.coinglass.com/' \
#     --header 'coinglassSecret: apiKey'

