class NotDateLogString(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("It's not date log string")

class NotValidLogsDateFormat(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__("Not valid datetime string format, format is hh:mm DD/MM/YYYY")