from pydantic import BaseModel
from src.core.enums import CloudTypeEnum


class ProviderSchema(BaseModel):
    id: int
    name: CloudTypeEnum
    provider_name: str


class ProviderCreateSchema(BaseModel):
    abbreviation: CloudTypeEnum
    provider_name: str
