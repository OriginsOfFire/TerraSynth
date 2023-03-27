from typing import TypeVar, Type

from fastapi import HTTPException
from pydantic import BaseModel

from src.core.db.db import Base
from src.core.exception.base_exception import ObjectNotFoundError

TableType = TypeVar('TableType', bound=Base)
CreateBaseSchema = TypeVar('CreateBaseSchema', bound=BaseModel)
UpdateBaseSchema = TypeVar('UpdateBaseSchema', bound=BaseModel)


class BaseMixin:
    table: TableType = None
    create_schema: CreateBaseSchema | None = None
    update_schema: UpdateBaseSchema | None = None

    @classmethod
    def unpack_filtered_fields(cls, filter_fields: dict) -> list:
        return [getattr(cls.table, name) == value for name, value in filter_fields.items()]

    @classmethod
    def _check_object(cls, obj: TableType) -> Type[HTTPException]:
        if not obj:
            raise ObjectNotFoundError()
