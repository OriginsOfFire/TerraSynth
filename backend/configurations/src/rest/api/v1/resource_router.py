from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from starlette.responses import JSONResponse

from src.core.db.db import get_db
from src.core.utils import encode_object_id
from src.models.resource_model import Resource
from src.rest.schemas.resource_schema import ResourceSchema
from src.services.resource_service import ResourceService

resource_router = APIRouter(prefix="/resources")


@resource_router.get("/", response_model=list[Resource])
async def get_resources(length: int = 10, db: AsyncIOMotorDatabase = Depends(get_db)):
    resources = await ResourceService.get_resources(length=length, db=db)
    for r in resources:
        r["_id"] = encode_object_id(r["_id"])["$oid"]
    return JSONResponse(status_code=200, content=resources)


@resource_router.post("/", response_model=Resource)
async def add_resource(
    data: ResourceSchema, db: AsyncIOMotorDatabase = Depends(get_db)
):
    resource = await ResourceService.add_resource(data=data, db=db)
    resource["_id"] = encode_object_id(resource["_id"])["$oid"]
    return JSONResponse(status_code=201, content=resource)
