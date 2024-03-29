from fastapi import APIRouter

from src.rest.api.v1.router import api_v1_router

base_router = APIRouter(prefix="/api")
base_router.include_router(api_v1_router)
