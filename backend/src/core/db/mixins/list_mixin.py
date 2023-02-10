from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin


class ListMixin(BaseMixin):
    @classmethod
    async def list(cls, session: AsyncSession):
        objects = await session.execute(
            select(cls.table)
        )
        return objects.scalar().all()