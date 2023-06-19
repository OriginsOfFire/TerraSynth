from typing import Any

from pydantic import BaseModel

from src.core.enums import DataTypeEnum


class BasicAttrModel(BaseModel):
    name: str
    data_type: DataTypeEnum


class AttributeModel(BasicAttrModel):
    pass


class ArgumentModel(BasicAttrModel):
    pass


class BasicInitAttrModel(BaseModel):
    name: str
    data_type: DataTypeEnum
    value: Any


class InitAttributeModel(BasicInitAttrModel):
    pass


class InitArgumentModel(BasicInitAttrModel):
    pass
