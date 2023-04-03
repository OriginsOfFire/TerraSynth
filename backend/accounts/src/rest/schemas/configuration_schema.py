from src.core.enums import CloudTypeEnum
from src.rest.schemas.base_schema import BaseSchema


class ConfigurationBaseSchema(BaseSchema):
    id: int | None
    user_id: int | None
    cloud_type: CloudTypeEnum | None


class ConfigurationCreateSchema(ConfigurationBaseSchema):
    user_id: int
    cloud_type: CloudTypeEnum


class ConfigurationUpdateSchema(ConfigurationBaseSchema):
    pass


class ConfigurationSchema(ConfigurationBaseSchema, BaseSchema):
    class Config:
        orm_mode = True
        fields = {'user': {'exclude': True}}
