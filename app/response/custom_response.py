from typing import Any

import orjson
from fastapi.responses import JSONResponse
from pydantic import BaseModel


def default(obj):
    return str(obj)


class CustomORJSONResponse(JSONResponse):
    """
    fastapi json response
    """

    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed"
        return orjson.dumps(content, default=default, option=orjson.OPT_INDENT_2)


class SuccessResponse(BaseModel):
    code: str
    message: str
    data: dict | list | None
