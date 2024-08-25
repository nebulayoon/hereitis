from fastapi import APIRouter

from app.response.custom_response import CustomORJSONResponse


class ErrorResponse:
    code: str
    message: str
    data: dict | list | None


router = APIRouter(
    default_response_class=CustomORJSONResponse,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)
