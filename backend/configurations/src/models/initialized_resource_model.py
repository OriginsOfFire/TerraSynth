from pydantic import Field

from src.models.argument_model import AttributeModel, InitArgumentModel
from src.models.base_model import BaseMongoModel, PyObjectId


class InitResource(BaseMongoModel):
    resource_id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    configuration_id: int
    arguments: list[InitArgumentModel]
    #attributes: list[AttributeModel]

