import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Worker(QThread):   # signal class

    signal1 = pyqtSignal(int, int)  # signal method -> 인수로는 슬롯으로 보내려는 값의 타입을 괄호안에 작성

    def run(self):
        self.signal1.emit(1000,2000)

class MainWindow(QMainWindow): # slot class
    def __int__(self):
        super().__init__()

        worker = Worker()

        worker.signal1.connect(self.slot1_signal1_print)

        worker.run()

    def slot1_signal1_print(self, btc, eth):  # slot method(function)
        print(f"비트코인가격:{btc}, 이더리움가격:{eth}")

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
























