import re

from PyQt5 import QtWidgets

from model import AnimationModel
from View import MainWindow


class Controller:
    def __init__(self, view, animation=AnimationModel()):
        self.animation = animation
        self.view = view
        self.view.OpenFile.clicked.connect(self.browse_file)
        self.view.StartAnimation.clicked.connect(self.start_animation)

    def browse_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        self.animation.file_path = file[0]

    def start_animation(self):
        pass

    def stop_animation(self):
        pass
