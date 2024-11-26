import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/comboBox.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_setting()
        self.comboBox.currentIndexChanged.connect(self.menu_select)
        # 콤보박스에서 사용자가 다른 메뉴를 선택하는 이벤트 발생시 호출될 메소드를 설정

    def comboBox_setting(self):  # 콤보박스 내용 설정
        dayList = ["월요일", "화요일", "수요일", "목요일", "금요일"]  # 콤보박스 메뉴에 사용될 값들을 리스트로 저장
        self.comboBox.addItems(dayList)  # 콤보박스에 리스트 타입으로 메뉴들 추가


    def menu_select(self): # 콤보박스 메뉴가 선택되었을때 호출되는 함수
        comboText = self.comboBox.currentText()  # 현재 콤보박스에서 선택한 값(문자열) 가져오기

        self.label.setText(comboText)  # 콤보박스에서 가져온 텍스트를 레이블에 출력하기

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
