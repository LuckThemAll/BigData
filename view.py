from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor, QPainter, QImage

import design


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.frame.paintEvent = self.framePaintEvent
        self.painter = QPainter(self.frame)
        self.currentImg = None
        self.newImage = None

    def setFrameSize(self, width, height):
        self.frame.setGeometry(QtCore.QRect(10, 50, width, height))
        self.currentImg = QImage(width, height, QImage.Format_RGB32)
        self.newImage = QImage(width, height, QImage.Format_RGB32)
        self.currentImg.fill(QColor(255, 255, 255))

    def setFrame(self, frame):
        x = 0
        y = 0
        index = 0
        if frame is not None:
            for _ in range(self.frame.width() * self.frame.height()):
                rgb_index = QColor(frame[index], frame[index + 1], frame[index + 2]).rgba()
                self.newImage.setPixel(x, y, rgb_index)
                index = index + 3
                x = x + 1
                if x == self.frame.width():
                    x = 0
                    y = y + 1
            self.currentImg = self.newImage

    def framePaintEvent(self, paint_event):
        self.painter.begin(self.frame)
        if self.currentImg is not None:
            self.painter.drawImage(0, 0, self.currentImg)
        self.painter.end()
        self.frame.update()
