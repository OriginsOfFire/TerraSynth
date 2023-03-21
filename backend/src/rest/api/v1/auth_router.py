from datetime import timedelta

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_401_UNAUTHORIZED

from src.core import settings
from src.core.db.db import get_session
from src.core.exception.base_exception import AuthenticationError
from src.rest.schemas.auth_schema import Token
from src.services.auth_service import AuthService

auth_router = APIRouter(tags=['auth'])


@auth_router.post('/token', response_model=Token)
async def get_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        session: AsyncSession = Depends(get_session),
) -> Token:
    user = await AuthService.authenticate_user(
        email=form_data.username,
        password=form_data.password,
        session=session
    )
    if not user:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail='Invalid credentials provided')
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await AuthService.create_access_token(
        data={'sub': user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type='bearer')

