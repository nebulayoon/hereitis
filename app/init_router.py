from fastapi import APIRouter
from pydantic import BaseModel

from app.api.v1.content_router import content_router
from app.response.custom_response import CustomORJSONResponse


class ErrorResponse(BaseModel):
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

router.include_router(content_router, prefix="", tags=["content"])
