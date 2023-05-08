from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import BaseMixin, TableType, CreateBaseSchema
from src.models import User


class CreateMixin(BaseMixin):
    @classmethod
    async def create(
        cls, input_data: CreateBaseSchema, session: AsyncSession
    ) -> TableType:
        obj = cls.table(**input_data.__dict__)
        session.add(obj)

        await session.commit()
        await session.refresh(obj)
        return obj
