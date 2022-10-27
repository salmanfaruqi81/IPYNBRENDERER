from email import message


class InvalidURLException(Exception):
    def __init__(self, message: str="URL is not valid"):
        super().__init__(self.message)
