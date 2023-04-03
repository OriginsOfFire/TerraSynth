from jose import jwt, ExpiredSignatureError, JWTError
from passlib.context import CryptContext

from src.core import settings
from src.core.exception.base_exception import InvalidTokenError

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


async def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


async def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)


async def decode_token(token: str) -> str:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get('sub')
    except (ExpiredSignatureError, JWTError, KeyError):
        raise InvalidTokenError
    return email
