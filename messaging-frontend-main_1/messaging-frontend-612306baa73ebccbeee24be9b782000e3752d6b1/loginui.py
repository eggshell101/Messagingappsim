import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox, QLineEdit, QLayout
from PySide6 import QtGui

from login import Ui_Dialog
from convui import ConvWindow

import requests


class LoginWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.onclick)
        self.commandLinkButton.clicked.connect(self.create)

        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.ip = '172.17.48.1'

        self.setWindowTitle('Login')
        width = 462
        height = 263
        self.setFixedSize(width, height)

    def onclick(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        key = int(requests.get(f'http://{self.ip}:5000/login/{username}/{password}/').text)
        if key == -1:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            msg = QMessageBox()
            msg.setText("Incorrect username or password")
            msg.exec()
            return
    
        self.window = ConvWindow(key, self.ip)
        self.window.show()
        super(LoginWindow, self).hide()
        
    def create(self):
        from createui import CreateWindow
        self.createwindow = CreateWindow(self.ip)
        self.createwindow.show()
        super(LoginWindow, self).destroy()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = LoginWindow()

    window.show()

    app.exec()
