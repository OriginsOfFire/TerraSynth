from fastapi import status


class BaseError(Exception):
    status_code: int
    default_detail: str
    default_headers: dict | None = None

    def __init__(self, detail: str = None, headers: dict = None):
        self.detail = detail
        self.headers = headers


class ObjectNotFoundError(BaseError):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Not found"