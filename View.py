import os

from PyQt5 import QtWidgets
from controller import Controller
import design


# from parser import Parser


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
