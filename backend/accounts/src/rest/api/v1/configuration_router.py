from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.core.db.db import get_session
from src.core.managers.configuration_manager import ConfigurationManager
from src.models import User
from src.rest.schemas.configuration_schema import (
    ConfigurationCreateSchema,
    ConfigurationSchema,
)
from src.services.auth_service import AuthService

configuration_router = APIRouter(tags=["configurations"])


@configuration_router.get("/configuration")
async def get_configurations(
    session: AsyncSession = Depends(get_session),
    user: User = Depends(AuthService.get_current_user),
) -> list:
    return await ConfigurationManager.list(
        session=session, filter_fields={"user_id": user.id}
    )


@configuration_router.post(
    "/configuration/",
    status_code=status.HTTP_201_CREATED,
    response_model=ConfigurationSchema,
)
async def create_configuration(
    input_data: ConfigurationCreateSchema,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(AuthService.get_current_user),
):
    input_data.id = user.id

    return await ConfigurationManager.create(input_data=input_data, session=session)


@configuration_router.delete(
    "/configuration/{config_id}", status_code=status.HTTP_200_OK
)
async def delete_configuration(
    config_id: int,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(AuthService.get_current_user),
):
    return await ConfigurationManager.delete(session=session, id=config_id)
