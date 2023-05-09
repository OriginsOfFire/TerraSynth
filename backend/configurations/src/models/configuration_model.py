from pydantic import Field

from src.models.base_model import BaseMongoModel, PyObjectId


class Configuration(BaseMongoModel):
    user_id: int
    name: str
    provider_id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    provider_version: str
