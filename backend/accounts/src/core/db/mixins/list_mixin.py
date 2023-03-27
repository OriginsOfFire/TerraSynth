from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin


class ListMixin(BaseMixin):
    @classmethod
    async def list(
            cls,
            session: AsyncSession,
            filter_fields: dict = {},
            search_fields: tuple | list = (),
    ):
        objects = await session.execute(
            select(cls.table).
            filter_by(**filter_fields).
            where(*search_fields)
        )
        return objects.scalars().all()
