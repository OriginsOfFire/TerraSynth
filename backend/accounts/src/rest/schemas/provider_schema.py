from pydantic import BaseModel
from src.core.enums import CloudTypeEnum


class ProviderSchema(BaseModel):
    id: int
    name: CloudTypeEnum
    provider_name: str


class ProviderCreateSchema(BaseModel):
    name: CloudTypeEnum
    provider_name: str
