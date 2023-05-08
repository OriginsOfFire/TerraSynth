from pydantic import Field

from src.models.argument_model import AttributeModel, ArgumentModel
from src.models.base_model import BaseMongoModel, PyObjectId


class Resource(BaseMongoModel):
    provider_id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    arguments: list[ArgumentModel]
    attributes: list[AttributeModel]
