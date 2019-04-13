import random

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QColor, QPainter

import design


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.frame.paintEvent = self.framePaintEvent
        self.currentFrame = None
        self.paint = QPainter(self.frame)

    def setFrameSize(self, width, height):
        self.frame.setGeometry(QtCore.QRect(10, 50, width, height))

    def setFrame(self, frame):
        self.currentFrame = frame

    def framePaintEvent(self, paint_event):
        self.paint.begin(self.frame)
        x = 0
        y = 0
        index = 0
        if self.currentFrame is not None:  # and not self.painted
            print(len(self.currentFrame))
            for i in range(self.frame.width() * self.frame.height()):
                self.paint.setPen(
                    QColor(self.currentFrame[index], self.currentFrame[index + 1], self.currentFrame[index + 2]))
                index = index + 3
                self.paint.drawPoint(y, x)
                x = x + 1
                if x == self.frame.width():
                    x = 0
                    y = y + 1
        self.paint.end()
        self.frame.update()
