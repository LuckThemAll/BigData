from animation_model import Animation


class Controller:
    def __init__(self, animation=Animation()):
        self.animation = animation

    def set_animation_size(self, width, height):
        self.animation.width = width
        self.animation.height = height

    def set_file_path(self, file_path):
        self.animation.file_path = file_path
