import sys
import requests
from PySide6 import QtWidgets

from inputui import MainWindow
from conv import Ui_Dialog
from contact_editui import ContactEditWindow
from create_convui import CreateConvWindow
from PySide6.QtCore import QTimer

import ast

class ConvWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, key, ip):
        super(ConvWindow, self).__init__()
        self.setupUi(self)
        width = 162
        height = 519
        self.setFixedSize(width, height)

        self.hostip = ip
        self.listWidget.itemDoubleClicked.connect(self.DoubleClicked)
        self.pushButton.clicked.connect(self.AddPeople)
        self.pushButton_2.clicked.connect(self.leave)
        self.pushButton_3.clicked.connect(self.CreateConv)
        self.key = key
        self.username = requests.get("http://{}:5000/getusername/{}/".format(self.hostip, self.key)).text
        self.label.setText(self.username)
        self.refresh()

        timer = QTimer(self)
        timer.timeout.connect(self.refresh)
        timer.start(3000)

    def refresh(self):
        row = self.listWidget.currentRow()
        self.setConvids()
        self.listWidget.setCurrentRow(row)

    def setConvids(self):
        self.listWidget.clear()
        convids = ast.literal_eval(requests.get("http://{}:5000/getallconvs/{}".format(self.hostip,self.key)).text)
        self.listWidget.addItems(list(map(self.toConvName, convids)))        

    def toConvName(self,convid):
        name = requests.get("http://{}:5000/getconvname/{}".format(self.hostip,convid)).text
        return name

    def toConvId(self, conversation):
        convid = requests.get("http://{}:5000/getconvid/{}".format(self.hostip,conversation)).text
        return convid

    def DoubleClicked(self):
        conversation = ((self.listWidget.selectedItems())[0]).text()
        convid = int(self.toConvId(conversation))
        self.mw = MainWindow(self.key, convid, self.hostip, conversation)
        self.mw.show()

    def AddPeople(self):
        x = self.listWidget.selectedItems()[0]
        self.cew = ContactEditWindow(self.toConvId(x.text()),self.hostip, self.username)
        self.cew.show()

    def CreateConv(self):
        self.cc = CreateConvWindow(self.key,self.hostip,self.username)
        self.cc.show()

    def leave(self):
        conversation = ((self.listWidget.selectedItems())[0]).text()
        convid = int(self.toConvId(conversation))
        requests.post("http://{}:5000/removefromconvid/{}/{}".format(self.hostip,convid,self.key))
        self.setConvids()

        


