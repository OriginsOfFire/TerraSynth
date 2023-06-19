import json

import aio_pika
from aio_pika import Message
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import JSONResponse

from src.core.db.db import get_session
from src.core.managers.configuration_manager import ConfigurationManager

from src.core.managers.provider_manager import ProviderManager
from src.models import User
from src.rest.schemas.configuration_schema import (
    ConfigurationCreateSchema,
    ConfigurationSchema, ConfigurationUpdateSchema,
)
from src.services.auth_service import AuthService

configuration_router = APIRouter(tags=["configurations"])


@configuration_router.get("/configurations")
async def get_configurations(
    session: AsyncSession = Depends(get_session),
    user: User = Depends(AuthService.get_current_user),
) -> list[ConfigurationSchema]:
    return await ConfigurationManager.list(
        session=session, filter_fields={"user_id": user.id}
    )


@configuration_router.get("/configurations/{config_id}")
async def get_configuration(
    config_id: int,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(AuthService.get_current_user)
) -> ConfigurationSchema:
    return await ConfigurationManager.retrieve(session=session, id=config_id)


@configuration_router.post(
    "/configurations/",
    status_code=status.HTTP_201_CREATED,
    response_model=ConfigurationSchema,
)
async def create_configuration(
    input_data: ConfigurationCreateSchema,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(AuthService.get_current_user),
):
    input_data.user_id = user.id
    provider = await ProviderManager.retrieve(session=session, name=input_data.cloud_type.value)
    input_data.provider_id = provider.id
    return await ConfigurationManager.create(input_data=input_data, session=session)


@configuration_router.put(
    "/configurations/{config_id}", status_code=status.HTTP_200_OK, response_model=ConfigurationSchema
)
async def update_configuration(
    config_id: int,
    input_data: ConfigurationUpdateSchema,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(AuthService.get_current_user),
):
    return await ConfigurationManager.update(update_data=input_data, session=session, pk=config_id)


@configuration_router.delete(
    "/configurations/{config_id}", status_code=status.HTTP_200_OK
)
async def delete_configuration(
    config_id: int,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(AuthService.get_current_user),
):
    connection = await aio_pika.connect("amqp://rabbitmq")
    channel = await connection.channel()
    await channel.declare_queue("configurations")
    await channel.default_exchange.publish(
        Message(json.dumps({"configuration_id": config_id}).encode("utf-8")),
        routing_key="configurations"
    )
    await connection.close()
    return await ConfigurationManager.delete(session=session, id=config_id)
