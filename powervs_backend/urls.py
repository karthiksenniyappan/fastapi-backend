from fastapi import APIRouter

from users.urls import users_router, auth_router

api_router = APIRouter(redirect_slashes=False)

api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
