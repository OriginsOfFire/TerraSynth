from fastapi import APIRouter

from src.rest.api.v1.configuration_router import configuration_router
from src.rest.api.v1.provider_router import provider_router
from src.rest.api.v1.resource_router import resource_router

api_v1_router = APIRouter(prefix="/v1")

api_v1_router.include_router(resource_router)
api_v1_router.include_router(provider_router)
api_v1_router.include_router(configuration_router)
