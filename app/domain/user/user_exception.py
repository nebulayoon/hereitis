from app.core.exception.custom_exception import CustomException
from fastapi import status


class UserExistsException(CustomException):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = "user exists"


class PasswordDoesNotMatchException(CustomException):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = "password does not match"


class UserNotFoundException(CustomException):
    status_code: int = status.HTTP_404_NOT_FOUND
    message: str = "user not found"


class WrongEmailorPasswordException(CustomException):
    status_code: int = status.HTTP_400_BAD_REQUEST
    message: str = "no email or wrong password"
