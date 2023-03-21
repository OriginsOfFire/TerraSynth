from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


async def verify_password(plain_password: str, hashed_password: str):
    print(plain_password, hashed_password)
    return pwd_context.verify(plain_password, hashed_password)


async def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)
