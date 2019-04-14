import threading
from PyQt5 import QtWidgets
from model import AnimationModel


class Controller:
    def __init__(self, view, animation=AnimationModel()):
        self.animation = animation
        self.view = view
        self.view.OpenFile.clicked.connect(self.browse_file)
        self.view.StartAnimation.clicked.connect(self.start_animation)
        self.stop_animation = False

    def browse_file(self):
        self.stop_animation = True
        file = QtWidgets.QFileDialog.getOpenFileName(self.view, "Выберите файл")
        self.animation.set_file_path(file[0])
        self.animation.get_info()
        self.view.set_frame_size(self.animation.width, self.animation.height)
        self.stop_animation = False

    def start_animation(self):
        if self.animation.is_meta_loaded:
            frame = self.animation.get_frame()
            self.view.set_frame(frame)
            if not self.stop_animation:
                threading.Timer(0.01, self.start_animation).start()
