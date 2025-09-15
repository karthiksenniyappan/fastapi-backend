from fastapi import Request, HTTPException

from core.security import generate_password_hash, compare_password
from users.models import User
from users.schema import UserTokenSchema, UserCreate


class UserViewSet:

    @staticmethod
    async def get_me():

        return {"name": "Hello"}

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
    async def login(request: Request):
        data = await request.json()
        user = await User.filter(username=data["username"]).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        check = compare_password(data["password"], user.password)
        if not check:
            raise HTTPException(status_code=404, detail="Incorrect password")
        return await UserTokenSchema.from_tortoise_orm(user)