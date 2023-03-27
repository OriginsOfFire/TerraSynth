from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


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
from src.core.error_handlers import * # noqa
