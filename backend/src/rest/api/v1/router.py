from fastapi import APIRouter

from src.rest.api.v1.user_router import user_router

api_v1_router = APIRouter(prefix='/v1')
api_v1_router.include_router(user_router)
