# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_1.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(279, 285)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartAnimation = QtWidgets.QPushButton(self.centralwidget)
        self.StartAnimation.setEnabled(True)
        self.StartAnimation.setGeometry(QtCore.QRect(140, 10, 114, 34))
        self.StartAnimation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartAnimation.setObjectName("StartAnimation")
        self.OpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFile.setGeometry(QtCore.QRect(10, 10, 121, 34))
        self.OpenFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OpenFile.setObjectName("OpenFile")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 50, 241, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartAnimation.setText(_translate("MainWindow", "Старт\n"
"Анимации"))
        self.OpenFile.setText(_translate("MainWindow", "Открыть\n"
"Файл"))


