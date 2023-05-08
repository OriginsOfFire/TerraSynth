from fastapi import FastAPI

from src.rest.api.v1.router import api_v1_router

app = FastAPI()
app.include_router(api_v1_router)
