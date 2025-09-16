from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel, EmailStr, Field

from users.models import User

UserTokenSchema = pydantic_model_creator(User, name="UserTokenSchema",
                                         include=('id', 'email', 'first_name', 'last_name'))


class UserCreate(BaseModel):
    first_name: str = Field(..., example="Admin")
    last_name: str = Field(..., example="A")
    username: str = Field(..., example="admin")
    email: EmailStr = Field(..., example="admin@starsystems.in")
    password: str = Field(..., min_length=6, example="demo@2025")


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"