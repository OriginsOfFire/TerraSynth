from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.app import app
from src.core.db.db import get_db
from src.models.resource_model import Resource
from src.rest.schemas.resource_schema import ResourceSchema


class ResourceService:
    @staticmethod
    async def get_resources(length: int, db: AsyncIOMotorDatabase = Depends(get_db)):
        return await db["resources"].find().to_list(length=length)

    @staticmethod
    async def add_resource(
            data: ResourceSchema, db: AsyncIOMotorDatabase = Depends(get_db)
    ) -> Resource:
        data = jsonable_encoder(data)
        new_resource = await db["resources"].insert_one(data)
        resource = await db["resources"].find_one({"_id": new_resource.inserted_id})
        return resource
