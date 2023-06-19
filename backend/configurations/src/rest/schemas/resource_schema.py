from pydantic import BaseModel

from src.models.argument_model import AttributeModel, ArgumentModel, InitArgumentModel, InitAttributeModel
from src.models.base_model import BaseMongoModel


class ResourceSchema(BaseMongoModel):
    provider_id: str
    name: str
    arguments: list[ArgumentModel]
    attributes: list[AttributeModel]


class InitResourceSchema(BaseMongoModel):
    resource_id: str
    name: str
    configuration_id: int
    arguments: list[InitArgumentModel]
    #attributes: list[InitAttributeModel]
