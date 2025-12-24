import os


class CleanUpFile:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type: None, exc_value: None, traceback: None):
        if os.path.exists("file.txt"):
            os.remove("file.txt")
