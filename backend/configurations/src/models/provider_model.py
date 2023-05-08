from pydantic import Field

from src.models.base_model import BaseMongoModel


class Provider(BaseMongoModel):
    name: str = Field(...)
    abbreviation: str = Field(...)
