import re
import time

class Parser:
    def __init__(self):
        self.file = None
        self.file_handle = 0
        self.start_frame_handle = 0

    def set_file(self, file_path):
        if file_path:
            self.file = open(file_path, "r")

    def read_animation_info(self):
        self.file.seek(0, 0)
        min_block_size = 52
        block = self.file.read(min_block_size)
        while block[-1:] != "[":
            block = block + self.file.read(1)
        width, height, frames = [int(s) for s in re.findall(r'\b\d+\b', block)]
        self.file_handle, self.start_frame_handle = self.file.tell() + 1, self.file.tell() + 1
        return width, height, frames

    def read_frame(self, width, height, is_last_frame=False):
        start_time = time.time()
        self.file.seek(self.file_handle, 0)
        min_block_size = 14 * width * height
        block = self.file.read(min_block_size)
        while block[-2:] != "]]":
            block = block + self.file.read(1)
        rgb_list = [int(s) for s in re.findall(r'\b\d+\b', block)]
        if is_last_frame:
            self.file_handle = self.start_frame_handle
        else:
            self.file_handle = self.file.tell() + 1
        print("--- %s seconds ---" % (time.time() - start_time))
        return rgb_list
