# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from PyQt5.QtCore import QAbstractTableModel, Qt
import cv2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1190, 889)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imageViewLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageViewLabel.setGeometry(QtCore.QRect(20, 100, 640, 480))
        self.imageViewLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imageViewLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageViewLabel.setObjectName("imageViewLabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 771, 71))
        self.label_2.setObjectName("label_2")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(280, 640, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")

        #--------- start btn
        self.start_btn.clicked.connect(self.onClicked)
        #-----

        self.teamMembers_btn = QtWidgets.QPushButton(self.centralwidget)
        self.teamMembers_btn.setGeometry(QtCore.QRect(30, 590, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.teamMembers_btn.setFont(font)
        self.teamMembers_btn.setObjectName("teamMembers_btn")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 670, 221, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(750, 550, 361, 171))
        self.tableView.setObjectName("tableView")

        ####### table data
        data = {"player name": ["player1", "computer"],
                "score": [0, 0]}
        df = pd.DataFrame(data)
        model = pandasModel(df)
        self.tableView.setModel(model)
        #######

        self.displayText_btn = QtWidgets.QTextBrowser(self.centralwidget)
        self.displayText_btn.setGeometry(QtCore.QRect(170, 750, 461, 51))
        self.displayText_btn.setObjectName("displayText_btn")
        self.icon_label = QtWidgets.QLabel(self.centralwidget)
        self.icon_label.setGeometry(QtCore.QRect(810, 20, 271, 221))
        self.icon_label.setFrameShape(QtWidgets.QFrame.Box)
        self.icon_label.setObjectName("icon_label")
        self.computer_display_lbl = QtWidgets.QLabel(self.centralwidget)
        self.computer_display_lbl.setGeometry(QtCore.QRect(840, 290, 200, 200))
        self.computer_display_lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.computer_display_lbl.setObjectName("computer_display_lbl")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(870, 490, 151, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 580, 131, 31))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def onClicked(self):
        cap=cv2.VideoCapture(0)
        cap.set(3,640)
        cap.set(4,480)
        cap.set(10,100)
        while(cap.isOpened()):
            success,img=cap.read()
            if success==True:
                cv2.imshow("player video",img)
            if cv2.waitKey(1)&0xff==ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SIP PROJECT"))
        self.imageViewLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">HAND CRICKET GAME </span></p></body></html>"))
        self.start_btn.setText(_translate("MainWindow", "START GAME"))
        self.teamMembers_btn.setText(_translate("MainWindow", "Team members"))
        self.pushButton_2.setText(_translate("MainWindow", "Instructions"))
        self.icon_label.setText(_translate("MainWindow", "TextLabel"))
        self.computer_display_lbl.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">computer value</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Player value</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()


    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
