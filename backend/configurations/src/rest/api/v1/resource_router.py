import io
import os.path
import zipfile

from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from starlette.responses import JSONResponse, Response, StreamingResponse, FileResponse

from src.core.db.db import get_db
from src.core.utils import encode_object_id
from src.models.initialized_resource_model import InitResource
from src.models.resource_model import Resource
from src.rest.schemas.resource_schema import ResourceSchema, InitResourceSchema
from src.services.resource_service import ResourceService

resource_router = APIRouter(prefix="/resources")


@resource_router.get("/", response_model=list[Resource])
async def get_resources(provider_id: int, db: AsyncIOMotorDatabase = Depends(get_db)):
    resources = await ResourceService.get_resources(provider_id=provider_id, length=10, db=db)
    return JSONResponse(status_code=200, content=resources)


@resource_router.post("/", response_model=Resource)
async def add_resource(
    data: ResourceSchema, db: AsyncIOMotorDatabase = Depends(get_db)
):
    resource = await ResourceService.add_resource(data=data, db=db)
    # resource["_id"] = encode_object_id(resource["_id"])["$oid"]
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


@resource_router.get("/initialize", response_model=InitResource)
async def get_initialized_resource(
    resource_id: str,
    db: AsyncIOMotorDatabase = Depends(get_db)
):
    resource = await ResourceService.retrieve_resource(resource_id=resource_id, db=db)

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
    root_module = 'terraform {\n required_version = ">= 1.0"\n}\n'
    resources = await ResourceService.get_initialized_resources(
        configuration_id=config_id, db=db
    )
    filenames = ["./user3/main.tf"]
    if not os.path.exists("./user3"):
        os.mkdir("./user3")

    for r in resources:
        module_def = f'module "{r["name"]}" {{\n'
        module_def += f'\tsource = "./modules/{r["name"]}"\n'
        module_def += "}\n"
        root_module += module_def
        s = "resource {} {{\n".format(r["name"])
        for argument in r["arguments"]:
            s += "\t{} = {}\n".format(argument["name"], argument["value"])
        s += "}"
        filename = f"./user3/{r['name']}/main.tf"
        filenames.append(filename)
        if not os.path.exists(f'./user3/{r["name"]}'):
            os.mkdir(f'./user3/{r["name"]}')
        with open(filename, "w+") as file:
            file.write(s)
    with open(f"./user3/main.tf", "w+") as file:
        file.write(root_module)
    print(filenames)
    archive_name = "./tfcode"
    import shutil
    file = shutil.make_archive(archive_name, 'zip', "./user3")
    resp = FileResponse(file, media_type="application/x-zip-compressed")
    return resp
