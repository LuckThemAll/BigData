from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QColor

import design


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 50, 241, 201))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QtWidgets.QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        self._image = QtGui.QPixmap("C:/Users/Artem/Desktop/oEpSN.png")

    def paintEvent(self, paint_event):
        pinter = QtGui.QPainter(self.paintField)
        pinter.begin(self.paintField)
        pinter.setBrush(QColor(200, 0, 0))
        pinter.drawRect(10, 15, 90, 60)
        pinter.end()
        # self.scene.drawBackground(pinter, QRectF())
        # self.scene.addPixmap(self._image)
        # self.retranslateUi(self)
