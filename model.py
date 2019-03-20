from myparser import Parser


class AnimationModel:
    def __init__(self, width=3, height=3):
        self.width = width
        self.height = height
        self.frames_num = 0
        self.current_frame = 0
        self.file_path = ""
        self.parser = Parser()

    def get_info(self):
        pass

    def get_pixel(self):
        pass

    def get_frame(self):
        pass

    def draw_frame(self):
        pass
