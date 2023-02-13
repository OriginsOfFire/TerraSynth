from fastapi import Request
from fastapi.responses import JSONResponse

from src.app import app
from src.core.exception.base_exception import InvalidTokenError


@app.exception_handler(InvalidTokenError)
async def invalid_token_handler(request: Request, exception: InvalidTokenError) -> JSONResponse:
    return JSONResponse(
        status_code=exception.status_code,
        content={'detail': exception.detail}
    )
