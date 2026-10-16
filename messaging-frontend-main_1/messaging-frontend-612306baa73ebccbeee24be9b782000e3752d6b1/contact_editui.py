from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox

from contact_edit import Ui_Dialog
import requests
import ast

class ContactEditWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, convid, ip, username):
        super(ContactEditWindow, self).__init__()
        self.setupUi(self)
        self.convid = convid
        self.pushButton.clicked.connect(self.addUser)
        self.pushButton_2.clicked.connect(self.deleteUser)
        self.pushButton_3.clicked.connect(self.save)
        self.pushButton_4.clicked.connect(self.destroy)
        self.ip = ip
        self.usernames = requests.get('http://{}:5000/getusers/{}'.format(self.ip,self.convid)).text
        self.userlist = ast.literal_eval(self.usernames.strip())
        self.listWidget.addItems(self.userlist)
        self.username = username

        self.delta = []


    def addUser(self):
        inp = self.textEdit.toPlainText()
        if inp not in self.userlist+self.delta:
            self.listWidget.addItem(inp)
            self.delta += [inp]
        self.textEdit.setText('')

    def deleteUser(self):
        self.listWidget.takeItem(self.listWidget.row(self.listWidget.selectedItems()[0]))

    def save(self):

        itemlist = []
        i = 0

        while True:
            try:
                item = self.listWidget.item(i).text()
            except:
                break
            i += 1
            if requests.get('http://{}:5000/exists/{}'.format(self.ip,item)).text == '':
                msg = QMessageBox()
                msg.setText("No account exists with the username '{}'.".format(item))
                msg.exec()
                return
            if item not in self.userlist:
                requests.post('http://{}:5000/addtoconv/{}/{}'.format(self.ip,self.convid,item))               
                requests.post('http://{}:5000/putmsg/{}/{}/{}'.format(self.ip,self.convid,20,self.username+' added '+item+'.'))
            itemlist.append(item)

        print(itemlist,self.userlist)

        for user in self.userlist:
            ct = self.userlist.count(user) - 1

            if ct > 0:
                requests.post('http://{}:5000/removefromconv/{}/{}'.format(self.ip,self.convid,user))
                requests.post('http://{}:5000/addtoconv/{}/{}'.format(self.ip,self.convid,user))

            if user not in itemlist:
                requests.post('http://{}:5000/removefromconv/{}/{}'.format(self.ip,self.convid,user))
                requests.post('http://{}:5000/putmsg/{}/{}/{}'.format(self.ip,self.convid,20,self.username+' removed '+user+'.'))

        self.destroy()

    def destroy(self):
        super(ContactEditWindow, self).destroy()

    

'''app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
'''
