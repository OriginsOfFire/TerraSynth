from fastapi import Request
from fastapi.responses import JSONResponse

from src.app import app
from src.core.exception.base_exception import (
    WrongCredentialsError,
    InvalidTokenError,
    ObjectNotFoundError,
)


@app.exception_handler(WrongCredentialsError)
async def wrong_credentials_error_handler(
    request: Request, exception: WrongCredentialsError
) -> JSONResponse:
    return JSONResponse(
        status_code=exception.status_code,
        content={"detail": exception.detail},
        headers=exception.headers,
    )


@app.exception_handler(InvalidTokenError)
async def invalid_token_error_handler(
    request: Request, exception: InvalidTokenError
) -> JSONResponse:
    return JSONResponse(
        status_code=exception.status_code,
        content={"detail": exception.detail},
        headers=exception.headers,
    )


@app.exception_handler(ObjectNotFoundError)
async def object_not_found_error_handler(
    request: Request, exception: ObjectNotFoundError
) -> JSONResponse:
    return JSONResponse(
        status_code=exception.status_code,
        content={"detail": exception.detail},
        headers=exception.headers,
    )
