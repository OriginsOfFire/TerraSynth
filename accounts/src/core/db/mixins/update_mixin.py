from fastapi import HTTPException
from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin, TableType, UpdateBaseSchema


class UpdateMixin(BaseMixin):
    @classmethod
    async def update(cls, pk: int, update_data: UpdateBaseSchema, session: AsyncSession) -> TableType | HTTPException:
        await session.execute(
            update(cls.table).
            where(cls.table.id == pk).
            values(**update_data)
        )
        await session.commit()

        result = await session.execute(
            select(cls.table).
            filter(cls.table.id == pk)
        )
        return result.scalars().first()
