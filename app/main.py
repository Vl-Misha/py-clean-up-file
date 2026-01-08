import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type: None, exc_value: None, traceback: None):
        try:
            os.remove(self.filename)

        except FileNotFoundError:
            pass

        except PermissionError:
            pass
