import orjson
from typing import Any
from fastapi.responses import JSONResponse


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
