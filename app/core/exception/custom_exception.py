from abc import ABC


class CustomException(ABC, Exception):
    """AbstractException"""

    status_code: int
    message: str

    def __init__(self, message=None):
        if message:
            self.message = message
