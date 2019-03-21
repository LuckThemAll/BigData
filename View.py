import os

from PyQt5 import QtWidgets
import design

class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def update_view(self, frame):
        pass