from datetime import timedelta

from fastapi import Request, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from core.security import generate_password_hash, compare_password, create_access_token, create_refresh_token
from powervs_backend.config import settings
from users.models import User
from users.schema import UserTokenSchema, UserCreate


class UserViewSet:

    @staticmethod
    async def get_me(currentUser):

        return currentUser

    @staticmethod
    async def get_all_users():

        return []

    @staticmethod
    async def create_user(request: UserCreate, role: str):
        data = request.model_dump()
        print(role)
        password = generate_password_hash(data["password"])
        payload = {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "email": data["email"],
            "password": password,
            "username": data["username"],
            "phone_number": None,
        }

        user = await User.create(**payload)

        return UserTokenSchema.from_tortoise_orm(user)

class AuthViewSet:

    @staticmethod
    async def login(data: OAuth2PasswordRequestForm):
        user = await User.filter(username=data.username).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        check = compare_password(data.password, user.password)
        if not check:
            raise HTTPException(status_code=404, detail="Incorrect password")
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token_expires = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

        access_token = create_access_token(
            data={"sub": str(user.id)}, expires_delta=access_token_expires
        )
        refresh_token = create_refresh_token(
            data={"sub": str(user.id)}, expires_delta=refresh_token_expires
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
