import requests
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time


class UpbitApi(QThread):  # 시그널 클래스->스레드 클래스

    coinDataSent = pyqtSignal(float, float)  # 시그널 함수->슬롯 함수에 데이터 전송

    def run(self):
        while True: # 무한루프(3초에 한번씩 실행)
            server_url = "https://api.upbit.com"
            params = {
                "markets": "KRW-BTC"
            }
            res = requests.get(server_url + "/v1/ticker", params=params)
            # print(res.json())
            btc_info = res.json()
            # print(btc_info[0]["trade_price"])  # 비트코인의 현재가격
            trade_price = btc_info[0]["trade_price"]  # 비트코인의 현재가격
            signed_change_rate = btc_info[0]["signed_change_rate"]  # 비트코인의 가격 변화율

            self.coinDataSent.emit(trade_price, signed_change_rate)  # 시그널 함수인 coinDataSenet 가져온 btc 가격 데이터를 제출

            time.sleep(3)  # 업비트 호출하는 딜레이 3초로 설정


class MainWindow(QMainWindow):  # 슬롯 클래스
    def __init__(self):
        super().__init__()

        self.upbitapi = UpbitApi()  # 시그널 클래스로 객체 생성

        self.upbitapi.coinDataSent.connect(self.printCoinData)
        self.upbitapi.run()

    def printCoinData(self, btcPrice, btcChangeRate):  # 슬롯 함수->시그널 함수에서 보내준 데이터를 받아주는 함수
        print(f"비트코인의 현재가격: {btcPrice}")
        print(f"비트코인의 가격변화율: {btcChangeRate}")


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())