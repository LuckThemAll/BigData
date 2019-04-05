import random

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

import design

class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.qp = QPainter()

    def update_view(self, frame):
        pass

    def initUI(self):
        self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self, e):

        self.qp.begin(self)
        self.qp.end()


