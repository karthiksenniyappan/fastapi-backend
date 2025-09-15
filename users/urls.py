from fastapi import APIRouter, Request, Query

from users.schema import UserCreate, UserTokenSchema
from users.views import UserViewSet, AuthViewSet

users_router = APIRouter()


@users_router.get("/")
async def get_me():
    return await UserViewSet.get_me()


@users_router.post("/", response_model=UserTokenSchema)
async def create_user(data: UserCreate, role: str = Query(default="user")):
    return await UserViewSet.create_user(data, role)


auth_router = APIRouter()


@auth_router.post("/login/")
async def login(request: Request):
    return await AuthViewSet.login(request)
