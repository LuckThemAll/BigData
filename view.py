from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor, QPainter, QImage, QPixmap

import design


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.frame.paintEvent = self.frame_paint_event
        self.painter = QPainter(self.frame)
        self.current_pixmap = None
        self.new_image = None

    def set_frame_size(self, width, height):
        self.frame.setGeometry(QtCore.QRect(10, 50, width, height))
        self.new_image = QImage(width, height, QImage.Format_RGB32)
        self.new_image.fill(QColor(255, 255, 255))
        self.current_pixmap = QPixmap(self.new_image)

    def set_frame(self, frame):
        x = 0
        y = 0
        index = 0
        if frame is not None:
            for _ in range(self.frame.width() * self.frame.height()):
                rgb_index = QColor(frame[index], frame[index + 1], frame[index + 2]).rgba()
                self.new_image.setPixel(x, y, rgb_index)
                index = index + 3
                x = x + 1
                if x == self.frame.width():
                    x = 0
                    y = y + 1
            self.current_pixmap = QPixmap(self.new_image)

    def frame_paint_event(self, paint_event):
        self.painter.begin(self.frame)
        if self.current_pixmap is not None:
            self.painter.drawPixmap(0, 0, self.current_pixmap)
        self.painter.end()
        self.frame.update()
