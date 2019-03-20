class Parser:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_file(self):
        return open(self.file_path, "r")
