class InvalidId(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class InvalidDate(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class InvalidInstallments(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)