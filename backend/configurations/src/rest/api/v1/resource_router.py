from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.core.utils import encode_object_id
from src.rest.schemas.resource_schema import ResourceSchema
from src.services.resource_service import ResourceService

resource_router = APIRouter(prefix="/resources")


@resource_router.get("/")
async def get_resources(length: int = 10):
    resources = await ResourceService.get_resources(length=length)
    for r in resources:
        r["_id"] = encode_object_id(r["_id"])["$oid"]
    return JSONResponse(status_code=200, content=resources)


@resource_router.post("/")
async def add_resource(data: ResourceSchema):
    resource = await ResourceService.add_resource(data=data)
    resource.id = encode_object_id(resource._id)["$oid"]
    return JSONResponse(status_code=201, content=resource)
