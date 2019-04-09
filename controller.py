import re

from PyQt5 import QtWidgets

from model import AnimationModel
from view import MainWindow


class Controller:
    def __init__(self, view, animation=AnimationModel()):
        self.animation = animation
        self.view = view
        self.view.OpenFile.clicked.connect(self.browse_file)
        self.view.StartAnimation.clicked.connect(self.start_animation)

    def browse_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self.view, "Выберите файл")
        self.animation.set_file_path(file[0])
        self.animation.get_info()

    def start_animation(self):
        if self.animation.is_meta_loaded:
            self.animation.draw_frame()

    def stop_animation(self):
        pass
