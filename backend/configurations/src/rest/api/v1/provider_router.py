from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from starlette.responses import JSONResponse

from src.core.db.db import get_db
from src.core.utils import encode_object_id
from src.models.provider_model import Provider
from src.services.provider_service import ProviderService

provider_router = APIRouter(prefix="/providers")


@provider_router.get("/", response_model=Provider)
async def get_providers(length: int = 10, db: AsyncIOMotorDatabase = Depends(get_db)):
    providers = await ProviderService.get_providers(length=length, db=db)
    for p in providers:
        p["_id"] = encode_object_id(p["_id"])["$oid"]
    return JSONResponse(status_code=200, content=providers)
