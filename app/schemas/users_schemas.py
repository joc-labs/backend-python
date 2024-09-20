from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password_hash: str
    is_active: bool = False
