from datetime import timedelta, datetime, UTC
from typing import Optional

from jose import jwt
from passlib.context import CryptContext

from powervs_backend.config import settings

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"


def generate_password_hash(password: str) -> str:
    """Generates a hashed password from the plain text password."""
    return password_context.hash(password)


def compare_password(password: str, _hash: str) -> bool:
    """Verifies a password against an existing hash."""
    return password_context.verify(secret=password, hash=_hash)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now(UTC) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now(UTC) + (expires_delta or timedelta(days=7))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.REFRESH_SECRET_KEY, algorithm=ALGORITHM)
