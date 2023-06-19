from pydantic import BaseModel

from src.core.enums import CloudTypeEnum
from src.rest.schemas.base_schema import BaseSchema


class ConfigurationBaseSchema(BaseSchema):
    id: int | None
    name: str | None
    user_id: int | None
    cloud_type: CloudTypeEnum | None
    provider_id: int | None


class ConfigurationCreateSchema(ConfigurationBaseSchema):
    user_id: int
    name: str
    cloud_type: CloudTypeEnum


class ConfigurationUpdateSchema(BaseModel):
    name: str | None
    cloud_type: CloudTypeEnum | None


class ConfigurationSchema(ConfigurationBaseSchema, BaseSchema):

    class Config:
        orm_mode = True
        fields = {"user": {"exclude": True}}


class ConfigurationsDeleteSchema(BaseSchema):
    ids: list[str]