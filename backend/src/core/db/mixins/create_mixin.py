from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin, TableType


class CreateMixin(BaseMixin):
    @classmethod
    async def create(cls, input_data, session: AsyncSession) -> TableType:
        obj = cls.table(**input_data)
        session.add(obj)

        await session.commit()
        await session.refresh(obj)
        return obj
