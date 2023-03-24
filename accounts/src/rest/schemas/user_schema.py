from pydantic import EmailStr, BaseModel

from src.rest.schemas.base_schema import BaseSchema


class UserBaseSchema(BaseModel):
    id: int | None
    email: EmailStr | None
    password: str | None
    full_name: str | None


class UserCreateSchema(UserBaseSchema):
    email: EmailStr
    password: str
    full_name: str


class UserUpdateSchema(UserBaseSchema):
    pass


class UserSchema(UserBaseSchema, BaseSchema):
    class Config:
        orm_mode = True
        fields = {'password': {'exclude': True}}

