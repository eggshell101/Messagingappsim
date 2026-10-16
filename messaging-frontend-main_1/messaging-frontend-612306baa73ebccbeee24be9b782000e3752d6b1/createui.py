import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox, QLineEdit

from create import Ui_Dialog
import requests
#from loginui import LoginWindow

class CreateWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, ip):
        super(CreateWindow, self).__init__()
        self.setupUi(self)
        
        self.ip = ip

        self.pushButton.clicked.connect(self.signup)
        self.commandLinkButton.clicked.connect(self.tologin)

        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.setWindowTitle('Sign up')
    def signup(self):
        password = self.lineEdit_2.text()
        username = self.lineEdit.text()
        password2 = self.lineEdit_3.text()

        if password == password2:
            res = requests.get(f"http://{self.ip}:5000/signup/{username}/{password}/").text
            msg = QMessageBox()

            if res == 'exists':
                msg.setText('An account with that username already exists.')
            else:
                msg.setText("Account creation successful.")

            msg.exec()
            self.tologin()
        else:
            msg = QMessageBox()
            msg.setText("Passwords do not match")
            msg.exec()
            return
        
    def tologin(self):
        from loginui import LoginWindow
        self.window = LoginWindow()
        self.window.show()
        super(CreateWindow,self).hide()

