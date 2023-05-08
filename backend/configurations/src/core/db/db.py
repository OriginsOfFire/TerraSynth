import motor.motor_asyncio

from src.core import settings

username = settings.MONGO_USERNAME
password = settings.MONGO_PASSWORD

client = motor.motor_asyncio.AsyncIOMotorClient(
    f"mongodb://{username}:{password}@{settings.MONGO_HOST}:{settings.MONGO_PORT}",
)
db = client.configurations


async def get_db() -> motor.motor_asyncio.AsyncIOMotorDatabase:
    yield db
