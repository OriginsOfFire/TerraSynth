from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.rest.schemas.provider_schema import ProviderSchema

from src.core.managers.provider_manager import ProviderManager

from src.models.user_model import User

from src.services.auth_service import AuthService

from src.core.db.db import get_session

provider_router = APIRouter(tags=["providers"])


@provider_router.get("/providers")
async def get_providers(
        session: AsyncSession = Depends(get_session),
        user: User = Depends(AuthService.get_current_user)
):
    return await ProviderManager.list(session=session)

