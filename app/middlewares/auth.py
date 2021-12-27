from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import HTTPException, status, Depends
from app.controllers import users
from pydantic import BaseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")


class User(BaseModel):
    name: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return users.verify_token(token, credentials_exception)
