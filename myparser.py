import re


class Parser:
    def __init__(self, file_path=""):
        self.file_path = file_path

    def get_file(self):
        if self.file_path:
            return open(self.file_path, "r")
        return None

    def read_block(self, size):
        with self.get_file() as f:
            block = f.read(size)
            arr = []
            for part in block.split(","):
                [arr.append(s) for s in re.findall(r'\b\d+\b', part)]
            del arr[3:]

    def get_animation_info(self):
        pass

    def read_pixel(self):
        pixel = {"r": None, "g": None, "b": None}
        return pixel


    # def get_pixels(self, nums=9):
    #     block = "....."
    #     block_offset = []
    #     with self.parser.get_file() as f:
    #         while block[len(block):-4] != "]]]}":
    #             if self.animation.file_handle:
    #                 pixels = {}
    #                 block = offset + f.read(100)
    #
    #                 offset = ""
    #             else:
    #                 step = 70
    #                 block = f.read(step)
    #                 arr = []
    #                 offset = block.split("[[[")[1]
    #                 for part in block.split(","):
    #                     [arr.append(s) for s in re.findall(r'\b\d+\b', part)]
    #                 del arr[3:]
    #                 self.animation.data_length = 49 + len(arr[0]) + len(arr[1]) + len(arr[2])
    #                 self.animation.width = int(arr[0])
    #                 self.animation.height = int(arr[1])
    #                 self.animation.frames = int(arr[2])
    #                 self.animation.file_handle = step
    #
    #             # if block == "":
    #             #     break
    #             print(offset)
    #             print(arr)

