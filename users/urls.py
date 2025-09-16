from fastapi import APIRouter, Request, Query, Depends
from fastapi.security import OAuth2PasswordRequestForm

from users.current_user import get_current_user
from users.schema import UserCreate, UserTokenSchema, TokenSchema
from users.views import UserViewSet, AuthViewSet

users_router = APIRouter()


@users_router.get("/me/")
async def get_me(currentUser = Depends(get_current_user)):
    return await UserViewSet.get_me(currentUser)


@users_router.post("/", response_model=UserTokenSchema)
async def create_user(data: UserCreate, role: str = Query(default="user")):
    return await UserViewSet.create_user(data, role)


auth_router = APIRouter()


@auth_router.post("/login/", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await AuthViewSet.login(form_data)
