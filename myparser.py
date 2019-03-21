import re


class Parser:
    def __init__(self):
        self.file = None

    def set_file(self, file_path):
        if file_path:
            self.file = open(file_path, "r")

    def read_block(self, size):
        with self.file as f:
            block = f.read(size)
            return block
            # arr = []
            # for part in block.split(","):
            #     [arr.append(s) for s in re.findall(r'\b\d+\b', part)]
            # del arr[3:]

    def read_animation_info(self):
        min_size = 52
        block = self.read_block(min_size)
        c = self.file.read(1)
        c = self.file.read(1)
        c = self.file.read(1)
        c = self.file.read(1)
        c = self.file.read(1)
        while True:
            c = self.file.read(1)#self.read_block(1)
            block = block + c
        arr = []
        [arr.append(int(s)) for s in re.findall(r'\b\d+\b', block)]
        return {"width": arr[0],
                "height": arr[1],
                "frames_num": arr[2],
                "start_frame_handle": self.file.tell() + 3}



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

