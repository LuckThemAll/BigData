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
        MainWindow.resize(264, 290)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 237, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OpenFile = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.OpenFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OpenFile.setObjectName("OpenFile")
        self.horizontalLayout.addWidget(self.OpenFile)
        self.StartAnimation = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.StartAnimation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartAnimation.setObjectName("StartAnimation")
        self.horizontalLayout.addWidget(self.StartAnimation)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.MainCanvas = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.MainCanvas.setObjectName("MainCanvas")
        self.verticalLayout.addWidget(self.MainCanvas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OpenFile.setText(_translate("MainWindow", "Открыть\nФайл"))
        self.StartAnimation.setText(_translate("MainWindow", "Старт\nАнимации"))


