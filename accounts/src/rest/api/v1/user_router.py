from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.managers.user_manager import UserManager
from src.rest.schemas.user_schema import UserSchema, UserCreateSchema
from src.services.auth_service import AuthService

user_router = APIRouter(tags=['users'])


@user_router.get('/user/me', response_model=UserSchema)
async def get_user(
        user=Depends(AuthService.get_current_user),
        session: AsyncSession = Depends(get_session)
):
    res = await UserManager.retrieve(id=user.id, session=session)
    return res


@user_router.get('/user', response_model=list[UserSchema])
async def get_users(
        session: AsyncSession = Depends(get_session)
):
    return await UserManager.list(session=session)


@user_router.post('/user/', response_model=UserSchema)
async def create_user(input_data: UserCreateSchema, session: AsyncSession = Depends(get_session)):
    return await UserManager.create(input_data=input_data, session=session)
