from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.managers.user_manager import UserManager
from src.rest.api.router import base_router
from src.rest.schemas.user_schema import UserCreateSchema, UserSchema, UserUpdateSchema
from src.services.auth_service import AuthService

app = FastAPI()
app.include_router(base_router)
