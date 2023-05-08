from pydantic import BaseModel

from src.models.argument_model import AttributeModel, ArgumentModel


class ResourceSchema(BaseModel):
    provider_id: str
    name: str
    arguments: list[ArgumentModel]
    attributes: list[AttributeModel]
