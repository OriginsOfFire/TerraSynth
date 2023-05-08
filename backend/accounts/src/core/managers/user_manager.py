from http.client import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.mixins.base_mixin import TableType
from src.core.managers.base_manager import CRUDManager
from src.core.utils import hash_password
from src.models import User
from src.rest.schemas.user_schema import UserCreateSchema, UserUpdateSchema


class UserManager(CRUDManager):
    table = User
    create_schema = UserCreateSchema
    update_schema = UserUpdateSchema

    @classmethod
    async def create(
        cls, input_data: UserCreateSchema, session: AsyncSession
    ) -> TableType:
        input_data.password = await hash_password(plain_password=input_data.password)
        return await super().create(input_data, session)

    @classmethod
    async def update(
        cls, pk: int, update_data: UserUpdateSchema, session: AsyncSession
    ) -> TableType | HTTPException:
        if update_data.get("password"):
            update_data.password = await hash_password(
                plain_password=update_data.password
            )
        return await super().update(pk, update_data, session)
