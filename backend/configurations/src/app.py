from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.rest.api.router import base_router

app = FastAPI()
app.include_router(base_router)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)