from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from starlette.responses import JSONResponse

from src.core.db.db import get_db
from src.core.utils import encode_object_id
from src.models.initialized_resource_model import InitResource
from src.models.resource_model import Resource
from src.rest.schemas.resource_schema import ResourceSchema, InitResourceSchema
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


@resource_router.post("/initialize", response_model=InitResource)
async def initialize_resource(
    data: InitResourceSchema, db: AsyncIOMotorDatabase = Depends(get_db)
):
    init_resource = await ResourceService.initialize_resource(data=data, db=db)
    init_resource["_id"] = encode_object_id(init_resource["_id"])["$oid"]
    return JSONResponse(status_code=201, content=init_resource)


@resource_router.get("/initialize", response_model=list[InitResource])
async def get_initialized_resources(
    configuration_id: int,
    db: AsyncIOMotorDatabase = Depends(get_db)
):
    init_resources = await ResourceService.get_initialized_resources(
        configuration_id=configuration_id, db=db
    )
    for resource in init_resources:
        resource["_id"] = encode_object_id(resource["_id"])["$oid"]
    return JSONResponse(status_code=200, content=init_resources)


@resource_router.post("/process-message")
async def process_message(message: dict, db: AsyncIOMotorDatabase = Depends(get_db)):
    configuration_id = message.get("configuration_id")
    if configuration_id:
        await db["init_resources"].delete_many({"configuration_id": configuration_id})
    return JSONResponse(status_code=200, content="deleted")


@resource_router.get("/generate/{config_id}")
async def generate_code(
        config_id: int,
        db: AsyncIOMotorDatabase = Depends(get_db)
):
    resources = await ResourceService.get_initialized_resources(
        configuration_id=config_id, db=db
    )
    result_strings = []
    for r in resources:
        s = "resource {} {{\n".format(r["name"])
        print(r)
        for argument in r["arguments"]:
            s += "\t{} = {}\n".format(argument["name"], argument["value"])
        s += "}"
        result_strings.append(s)
    return result_strings
