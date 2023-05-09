from bson import ObjectId
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase


class ProviderService:
    @staticmethod
    async def get_providers(
        length: int,
        db: AsyncIOMotorDatabase,
    ):
        return await db["providers"].find().to_list(length=length)

    @staticmethod
    async def retrieve_provider(
        provider_id: str,
        db: AsyncIOMotorDatabase,
    ):
        provider = await db["providers"].find_one(
            {"_id": {"$eq": ObjectId(provider_id)}}
        )
        if not provider:
            raise HTTPException(
                status_code=404, detail=f"Provider with id:{provider_id} not found"
            )
