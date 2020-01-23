class WeatherException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InputIsNotValid(Exception):
    def __init__(self, message):
        super().__init__(message)
