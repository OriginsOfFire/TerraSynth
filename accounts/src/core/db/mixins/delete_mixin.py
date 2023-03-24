from fastapi import HTTPException
from sqlalchemy import delete, and_
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin


class DeleteMixin(BaseMixin):
    @classmethod
    async def delete(cls, session: AsyncSession, **kwargs) -> dict | HTTPException:
        filter_fields = cls.unpack_filtered_fields(kwargs)

        await session.execute(
            delete(cls.table).
            where(and_(True, *filter_fields))
        )
        await session.commit()

        return {'status': 200}
