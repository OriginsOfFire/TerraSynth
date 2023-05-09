from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.rest.schemas.configuration_schema import ConfigurationSchema
from src.services.provider_service import ProviderService


class ConfigurationService:
    @staticmethod
    async def get_configurations(
        user_id: int, length: int, db: AsyncIOMotorDatabase
    ) -> list[dict]:
        configurations = (
            await db["configurations"]
            .find(
                {
                    "user_id": {"$eq": user_id},
                }
            )
            .to_list(length=length)
        )
        return configurations

    @staticmethod
    async def create_configuration(
        data: ConfigurationSchema, db: AsyncIOMotorDatabase
    ) -> dict:
        await ProviderService.retrieve_provider(provider_id=data.provider_id, db=db)
        data = jsonable_encoder(data)
        new_configuration = await db["configurations"].insert_one(data)
        return await db["configurations"].find_one(
            {"_id": new_configuration.inserted_id}
        )
