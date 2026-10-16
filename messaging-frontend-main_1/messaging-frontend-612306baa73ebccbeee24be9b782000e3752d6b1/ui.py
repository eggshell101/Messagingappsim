import sys
from PySide6 import QtWidgets

from untitled import Ui_Dialog


class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.msglist = self.getConvHist()

        self.pushButton.clicked.connect(self.writedata)
        self.textBrowser.setText(self.msglist)
        self.lineEdit.setPlaceholderText('Type here...')

    def writedata(self):
        self.msglist += 'Me: '+self.lineEdit.text()+'\n'
        self.textBrowser.setText(self.msglist)
        self.lineEdit.setText('')

    def getConvHist(self):
        return '''Me: hello
A: Hi!
Me: abc
'''
'''
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()'''
