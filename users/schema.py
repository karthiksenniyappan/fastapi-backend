from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel, EmailStr, Field

from users.models import User

UserTokenSchema = pydantic_model_creator(User, name="UserTokenSchema",
                                         include=('id', 'email', 'first_name', 'last_name'))


class UserCreate(BaseModel):
    first_name: str = Field(..., json_schema_extra={"example": "John"})
    last_name: str = Field(..., json_schema_extra={"example": "A"})
    username: str = Field(..., json_schema_extra={"example": "Admin"})
    email: EmailStr = Field(..., json_schema_extra={"example": "admin@example.com"})
    password: str = Field(..., min_length=6, json_schema_extra={"example": "password"})


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"