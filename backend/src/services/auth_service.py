from datetime import timedelta, datetime
from typing import Tuple

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, ExpiredSignatureError, JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import settings
from src.core.db.db import get_session
from src.core.exception.base_exception import AuthenticationError, InvalidTokenError
from src.core.managers.user_manager import UserManager
from src.core.utils import verify_password
from src.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


class AuthService:
    @classmethod
    async def authenticate_user(cls, user_data: dict, session: AsyncSession) -> User | HTTPException:
        password = user_data.pop('password')

        user = await UserManager.retrieve(session=session, **user_data)
        if verify_password(password, user.password):
            return user

        raise AuthenticationError()

    @classmethod
    def decode_token(cls, token: str):
        try:
            payload = jwt.decode(token=token, key=settings.SECRET_KEY, algorithms=settings.ALGORITHM)
            user_id = payload.get('sub')
        except (JWTError, ExpiredSignatureError, KeyError):
            raise InvalidTokenError()

        return user_id

    @classmethod
    async def create_access_token(cls, user_id: int, token_type: str) -> str:
        if token_type == 'access':
            expires_at = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        elif token_type == 'refresh':
            expires_at = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)

        payload = {
            'sub': user_id,
            'exp': expires_at,
        }
        encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    @classmethod
    async def generate_token_pair(cls, user_id: int) -> Tuple[str, str]:
        access_token = await cls.create_access_token(user_id=user_id, token_type='access')
        refresh_token = await cls.create_access_token(user_id=user_id, token_type='refresh')

        return access_token, refresh_token

    @classmethod
    async def generate_token_pair_on_refresh(cls, old_refresh_token: str) -> Tuple[str, str]:
        user_id = cls.decode_token(token=old_refresh_token)
        access_token, refresh_token = await cls.generate_token_pair(user_id=user_id)
        return access_token, refresh_token

    @classmethod
    async def get_current_user(
            cls,
            session: AsyncSession = Depends(get_session),
            token: str = Depends(oauth2_scheme)
    ) -> User:
        user_id = cls.decode_token(token=token)
        user = await UserManager.retrieve(session=session, id=user_id)
        return user
