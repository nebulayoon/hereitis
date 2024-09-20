from app.core.exception.custom_exception import CustomException
from fastapi import status


class NotValidateJWTTokenException(CustomException):
    status_code: int = status.HTTP_401_UNAUTHORIZED
    message: str = "Could not validate credentials"
