from fastapi import status

from app.core.exception.custom_exception import CustomException


class NotValidateJWTTokenException(CustomException):
    status_code: int = status.HTTP_401_UNAUTHORIZED
    message: str = "Could not validate credentials"
