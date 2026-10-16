import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer

from input import Ui_Dialog
import requests
from time import sleep

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, key, conversation, ip, convname):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.key = key
        self.conversation = conversation
        self.hostip = ip
        self.msglist = self.getConvHist()
        self.pushButton.clicked.connect(self.writedata)
        self.textBrowser.setText(self.msglist)
        self.lineEdit.setPlaceholderText('Type here...')
        self.setWindowTitle(convname)
        
        timer = QTimer(self)
        timer.timeout.connect(self.refresh)
        timer.start(3000)
        
    def refresh(self):
        self.msglist = self.getConvHist()
        pos = self.textBrowser.verticalScrollBar().value()

        self.textBrowser.setText(self.msglist)
        self.textBrowser.verticalScrollBar().setValue(pos)


    def writedata(self):
        requests.post("http://{}:5000/putmsg/{}/{}/{}".format(self.hostip,self.conversation, self.key, self.lineEdit.text().replace('/','\\')))
        self.refresh()
        self.lineEdit.setText('')
        
    def getConvHist(self):
        return requests.get("http://{}:5000/getmsgs/{}".format(self.hostip,self.conversation)).text
