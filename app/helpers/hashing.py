from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def bcrypt(password: str):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(password)
