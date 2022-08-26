class MessageException(Exception):

    def __init__(self, message=""):
        self.message = message
        super(MessageException, self).__init__()


class ZeroError(MessageException):

    def __str__(self):
        return f"zero division. {self.message}"


class ListNumberError(MessageException):

    def __str__(self):
        return f"Data in list is not int. {self.message}"


class NoPlaceError(MessageException):

    def __str__(self):
        return f"No more free space. {self.message}"


class NoItemError(MessageException):

    def __str__(self):
        return f"No such item. {self.message}"
