import os

from PyQt5 import QtWidgets
from controller import Controller

import design


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.OpenFile.clicked.connect(self.browse_file)
        self.controller = Controller()

    def browse_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        if file:
            self.controller.set_file_path(file)
