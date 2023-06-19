from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorDatabase


from src.rest.schemas.resource_schema import ResourceSchema, InitResourceSchema


class ResourceService:
    @staticmethod
    async def get_resources(provider_id: int, length: int, db: AsyncIOMotorDatabase) -> list[dict]:
        return await db["resources"].find({"provider_id": provider_id}).to_list(length=length)

    @staticmethod
    async def add_resource(data: ResourceSchema, db: AsyncIOMotorDatabase) -> dict:
        data = jsonable_encoder(data)
        new_resource = await db["resources"].insert_one(data)
        resource = await db["resources"].find_one({"_id": new_resource.inserted_id})
        return resource

    @staticmethod
    async def retrieve_resource(resource_id: str, db: AsyncIOMotorDatabase):
        return await db["resources"].find_one({"_id": resource_id})

    @staticmethod
    async def initialize_resource(data: InitResourceSchema, db: AsyncIOMotorDatabase) -> dict:
        data = jsonable_encoder(data)
        init_resource = await db["init_resources"].insert_one(data)
        resource = await db["init_resources"].find_one({"_id": init_resource.inserted_id})
        return resource

    @staticmethod
    async def get_initialized_resources(configuration_id: int, db: AsyncIOMotorDatabase) -> list[dict]:
        init_resources = await db["init_resources"].find({"configuration_id": configuration_id}).to_list(length=10)
        return init_resources
