from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin


class RetrieveMixin(BaseMixin):
    @classmethod
    async def retrieve(cls, session: AsyncSession, **kwargs: Any):
        filter_fields = cls.unpack_filtered_fields(filter_fields=kwargs)

        query = await session.execute(
            select(cls.table).
            where(*filter_fields)
        )
        obj = query.scalar_one_or_none()
        cls._check_object(obj=obj)

        await session.refresh(obj)
        return obj