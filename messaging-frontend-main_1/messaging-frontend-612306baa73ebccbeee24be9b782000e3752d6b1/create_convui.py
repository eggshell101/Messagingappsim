from PySide6 import QtWidgets
from create_conv import Ui_Dialog
import requests

class CreateConvWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, key, ip, username):
        super(CreateConvWindow, self).__init__()
        self.setupUi(self)

        self.key = key
        self.ip = ip
        self.username = username

        self.pushButton.clicked.connect(self.createconv)
        self.pushButton_2.clicked.connect(self.destroy)

    def createconv(self):
        convname = self.lineEdit.text()
        convid = int(requests.get("http://{}:5000/createconv/{}/{}".format(self.ip, convname, self.key)).text)
        requests.post('http://{}:5000/putmsg/{}/{}/{}'.format(self.ip,convid,20,self.username+' created this conversation.'))
        self.destroy()

    def destroy(self):
        super(CreateConvWindow, self).destroy()
