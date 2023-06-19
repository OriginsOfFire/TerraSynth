from pydantic import BaseModel

from src.models.argument_model import AttributeModel, ArgumentModel, InitArgumentModel, InitAttributeModel


class ResourceSchema(BaseModel):
    provider_id: str
    name: str
    arguments: list[ArgumentModel]
    attributes: list[AttributeModel]


class InitResourceSchema(BaseModel):
    resource_id: str
    name: str
    configuration_id: int
    arguments: list[InitArgumentModel]
    #attributes: list[InitAttributeModel]
