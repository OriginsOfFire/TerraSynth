from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from starlette.responses import JSONResponse

from src.core.db.db import get_db
from src.core.utils import encode_object_id
from src.models.configuration_model import Configuration
from src.rest.schemas.configuration_schema import ConfigurationSchema
from src.services.configuration_service import ConfigurationService

configuration_router = APIRouter(prefix="/configurations")


@configuration_router.get("/", response_model=list[Configuration])
async def get_configurations(
    user_id: int, length: int = 10, db: AsyncIOMotorDatabase = Depends(get_db)
):
    configurations = await ConfigurationService.get_configurations(
        user_id=user_id, length=length, db=db
    )
    for c in configurations:
        c["_id"] = encode_object_id(c["_id"])["$oid"]
    return JSONResponse(status_code=200, content=configurations)


@configuration_router.post("/", response_model=Configuration)
async def create_configuration(
    data: ConfigurationSchema, db: AsyncIOMotorDatabase = Depends(get_db)
):
    configuration = await ConfigurationService.create_configuration(data=data, db=db)
    configuration["_id"] = encode_object_id(configuration["_id"])["$oid"]
    return JSONResponse(status_code=201, content=configuration)
