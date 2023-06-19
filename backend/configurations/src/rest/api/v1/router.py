from fastapi import APIRouter

from src.rest.api.v1.resource_router import resource_router

api_v1_router = APIRouter(prefix="/v1")

api_v1_router.include_router(resource_router)
