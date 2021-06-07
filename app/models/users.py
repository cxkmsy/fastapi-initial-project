from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    is_active: bool


class UserCreate(UserBase):
    name: str
    email: str
    password: str


class UserUpdate(UserBase):
    name:  Optional[str] = None
    email:  Optional[str] = None
    password:  Optional[str] = None
    is_active: Optional[bool] = None


class User(UserBase):
    class Config:
        orm_mode = True
