from PyQt5.QtGui import QColor

from myparser import Parser
from view import MainWindow


class AnimationModel:
    def __init__(self):
        self.parser = Parser()
        self.width = 0
        self.height = 0
        self.frames_num = 0
        self.current_frame = 0
        self.file_path = ""
        self.is_meta_loaded = False

    def set_file_path(self, file_path):
        self.file_path = file_path
        self.parser.set_file(self.file_path)

    def get_info(self):
        self.width, self.height, self.frames_num = self.parser.read_animation_info()
        self.current_frame = 1
        self.is_meta_loaded = True

    def get_frame(self):
        frame = None
        if self.is_meta_loaded:
            frame = self.parser.read_frame(self.width, self.height, self.current_frame == self.frames_num)
            self.current_frame += 1
        return frame

    def draw_frame(self):
        pass
