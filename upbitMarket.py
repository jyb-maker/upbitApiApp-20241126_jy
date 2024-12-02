import requests
import pyupbit

url = "https://api.upbit.com/v1/market/all?is_details=true"

headers = {"accept": "application/json"}

res = requests.get(url, headers=headers)

print(res.json())

current_price =pyupbit.get_current_price("KRW-BTC")     # 해당 코인의 현재 가격
print(current_price)
tickerList = pyupbit.get_tickers(fiat="KRW")    # 코인 종류(원화가격표시) ticker 리스트 가져오기(리스트 타입으로 반환)
print(tickerList)





