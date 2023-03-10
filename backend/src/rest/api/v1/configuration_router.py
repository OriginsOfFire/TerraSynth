from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.core.db.db import get_session
from src.core.managers.configuration_manager import ConfigurationManager
from src.models import User
from src.services.auth_service import AuthService

configuration_router = APIRouter(tags=['configurations'])


@configuration_router.get('/configuration/')
async def get_configurations(
        session: AsyncSession = Depends(get_session),
        user: User = Depends(AuthService.get_current_user),
) -> list:
    return await ConfigurationManager.list(
        session=session,
        filter_fields={'user_id': user.id}
    )


@configuration_router.post('/configuration/', status_code=status.HTTP_201_CREATED)
async def create_configuration(
    session: AsyncSession = Depends(get_session),
    user: User = Depends(AuthService.get_current_user),
):
    pass
