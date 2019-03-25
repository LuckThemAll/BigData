from myparser import Parser
from View import MainWindow


class AnimationModel:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.frames_num = 0
        self.current_frame = 0
        self.file_path = ""
        self.parser = Parser()
        self.file_handle = 0
        self.start_frame_handle = 0
        self.is_meta_loaded = False

    def set_file_path(self, file_path):
        self.file_path = file_path
        self.parser.set_file(self.file_path)

    def get_info(self):
        info_dict = self.parser.read_animation_info()
        self.width = info_dict["width"]
        self.height = info_dict["height"]
        self.frames_num = info_dict["frames_num"]
        self.start_frame_handle = info_dict["start_frame_handle"]
        self.file_handle = self.start_frame_handle
        self.is_meta_loaded = True

    def get_pixel(self):
        pixel = self.parser.read_pixel()
        self.file_handle = pixel[1]
        return pixel


    def get_frame(self):
        self.frame = FrameStructure(self.width, self.height)
        pixels_num = self.width * self.height
        for i in range(pixels_num):
            pixel = self.get_pixel()
            self.frame.update_pixel(i, pixel)
        return self.frame

    def draw_frame(self):
        # self.
        pass


class FrameStructure:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = {}
        self.initialize_pixels()

    def initialize_pixels(self):
        for i in range(self.width * self.height):
            pixel = {"r": None, "g": None, "b": None}
            self.pixels[i] = pixel

    def update_pixel(self, pos, pixel):
        self.pixels[pos]["r"] = pixel["r"]
        self.pixels[pos]["g"] = pixel["g"]
        self.pixels[pos]["b"] = pixel["b"]
