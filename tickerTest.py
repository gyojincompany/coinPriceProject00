import requests
import pyupbit

url = "https://api.upbit.com/v1/market/all?isDetails=false"

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

ticker_list = pyupbit.get_tickers()
print(ticker_list)
