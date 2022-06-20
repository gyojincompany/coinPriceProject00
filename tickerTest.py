import pyupbit

ticker_list = pyupbit.get_tickers(fiat="KRW")
print(ticker_list)

coin_list = []
for ticker in ticker_list:
    #print(ticker[4:10])
    coin_list.append(ticker[4:10])

print(coin_list)