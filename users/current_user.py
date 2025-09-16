from fastapi import Depends, status, HTTPException
from jose import jwt, JWTError

from core.oauth2_password_bearer import get_oauth2_scheme
from core.schema import UserSchema, TokenData
from powervs_backend.config import settings
from users.models import User
from users.schema import UserTokenSchema

_oauth2_scheme = get_oauth2_scheme()

SECRET_KEY = settings.SECRET_KEY  # 🔐 replace with env var in prod
REFRESH_SECRET_KEY = settings.REFRESH_SECRET_KEY  # separate key for refresh tokens
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS = settings.REFRESH_TOKEN_EXPIRE_DAYS


async def get_current_user(token: str = Depends(_oauth2_scheme)) -> UserSchema:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate access token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        pk: int = payload.get("sub")
        if pk is None:
            raise credentials_exception
        token_data = TokenData(pk=pk)
    except JWTError:
        raise credentials_exception

    user = await User.filter(pk=token_data.pk).first()
    if user is None:
        raise credentials_exception
    user = await UserTokenSchema.from_tortoise_orm(user)
    return user
