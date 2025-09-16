from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str


class TokenData(BaseModel):
    pk: Optional[int] = None