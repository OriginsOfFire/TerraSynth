from pydantic import BaseModel

from src.core.enum import DataTypeEnum


class BasicAttrModel(BaseModel):
    name: str
    data_type: DataTypeEnum


class AttributeModel(BasicAttrModel):
    pass


class ArgumentModel(BasicAttrModel):
    pass
