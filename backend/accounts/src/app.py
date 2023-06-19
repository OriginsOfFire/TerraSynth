from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.types import Message

from src.rest.api.router import base_router

origins = [
    "*",
]



app = FastAPI()
app.include_router(base_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def set_body(request: Request, body: bytes):
    async def receive() -> Message:
        return {"type": "http.request", "body": body}

    request._receive = receive


async def get_body(request: Request) -> bytes:
    body = await request.body()
    await set_body(request, body)
    return body


@app.middleware("http")
async def app_entry(request: Request, call_next):
    await set_body(request, await request.body())

    print(await get_body(request))

    response = await call_next(request)
    return response

from src.core.error_handlers import * # noqa
