from PyQt5 import QtWidgets, uic
import os
from time import sleep
import pyautogui
from ui import a

pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True

path = os.getcwd()
qtCreatorFile = path + os.sep + "ui" + os.sep + "Main_Window.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MainUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.iniGuiEvent()

    def iniGuiEvent(self):
        self.btn1.clicked.connect(self.btn1_onClick)
        self.btn2.clicked.connect(self.btn2_onClick)
        self.btn3.clicked.connect(self.btn3_onClick)

    def btn1_onClick(self):
        a.xsite = []
        a.ysite = []
        sleep(1)
        pyautogui.size()

        for i in range(20):
            sleep(3)
            x, y = pyautogui.position()
            a.xsite.append(x)
            a.ysite.append(y)
            print(a.xsite, a.ysite)


    def btn2_onClick(self):
        a.time_list = []
        timer = open(r'C:\tmp\timer.txt', mode='r', encoding='utf-8').read()
        # ***************** 可輸入 000 代替 0:0:0 ***************
        times = timer.replace('000', '0:0:0').strip()
        ddd = times.split(',')
        if len(ddd) == 20:
            for i in range(len(ddd)):
                a.aas.append(ddd[i])
                self.to_times()

        else:
            print('請確定timer中的時間是否剛好是20個，或是輸入錯誤資料')


    def btn3_onClick(self):
        for i in range(19):
            pyautogui.click(a.xsite[i], a.ysite[i], button='left')
            sleep(a.time_list[i])
    def to_times(self):

        for rem in range(len(a.aas)):
            a.the_time = ''
            a.the_time = a.aas[rem]
            the_times = a.the_time.split(":")

        for e in range(len(the_times)):

            if e == 0:

                time_chage1 = int(the_times[e])

            elif e == 1:
                time_chage2 = int(the_times[e]) * 60
            else:
                time_chage3 = int(float(the_times[e])) * 3600
                time_chages = time_chage1 + time_chage2 + time_chage3
                a.time_list.append(time_chages)

                time_chage1 = 0
                time_chage2 = 0
                time_chage3 = 0
                time_chages = 0
        if a.time_list != []:
            print('讀取到時間了')
        else:
            print('請在C巢的timer中輸入時間')




