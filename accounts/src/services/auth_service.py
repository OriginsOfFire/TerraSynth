from datetime import timedelta, datetime

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import settings
from src.core.db.db import get_session
from src.core.exception.base_exception import WrongCredentialsError, InvalidTokenError
from src.core.managers.user_manager import UserManager
from src.core.utils import verify_password, decode_token
from src.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    @staticmethod
    async def create_access_token(data: dict, expires_delta: timedelta | None = None):
        payload = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=30)
        payload.update({'exp': expire})
        return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    @staticmethod
    async def authenticate_user(
            email: str,
            password: str,
            session: AsyncSession = Depends(get_session),
    ) -> bool | User:
        user = await UserManager.retrieve(session, email=email)

        if await verify_password(password, user.password):
            return user
        raise WrongCredentialsError

    @staticmethod
    async def get_current_user(
            token: str = Depends(oauth2_scheme),
            session: AsyncSession = Depends(get_session),
    ) -> User | HTTPException:
        email = await decode_token(token)
        user = await UserManager.retrieve(email=email, session=session)
        return user
