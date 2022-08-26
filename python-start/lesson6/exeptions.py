class MessageException(Exception):

    def __init__(self, message):
        self.message = message
        super(MessageException, self).__init__()


class ConfigError(MessageException):

    def __str__(self):
        return f"Error in config file. {self.message}"


class ModeError(MessageException):

    def __str__(self):
        return "Error in mode. Check your configuration"


class VelocityError(MessageException):

    def __str__(self):
        return self.message
