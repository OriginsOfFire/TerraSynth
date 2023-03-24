from fastapi import status


class BaseError(Exception):
    status_code: int
    default_detail: str
    default_headers: dict | None = None

    def __init__(self, detail: str = None, headers: dict = None):
        self.detail = detail or self.default_detail
        self.headers = headers or self.default_headers


class ObjectNotFoundError(BaseError):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Not found"


class WrongCredentialsError(BaseError):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Wrong credentials provided"


class InvalidTokenError(BaseError):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Invalid or expired token provided"
