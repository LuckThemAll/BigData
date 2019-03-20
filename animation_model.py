class Animation:
    def __init__(self, file_path="", width=3, height=3):
        self.width = width
        self.height = height
        self.file_path = file_path

    def get_file_path(self):
        if not self.file_path == "":
            return self.file_path[0]
        else:
            return None
