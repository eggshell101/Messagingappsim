# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contact_edit.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(384, 290)
        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 10, 251, 191))
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 210, 251, 31))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(270, 10, 111, 21))
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 40, 111, 21))
        self.pushButton_2.setFont(font)
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(110, 250, 71, 24))
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(190, 250, 71, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter username", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"ADD CONTACT", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"DELETE CONTACT", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

