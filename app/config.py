from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str  = "localhost"
    DB_PORT: str  = "3306"
    DB_NAME: str  = "test_db"
    DB_USER: str  = "root"
    DB_PASS: str  = "rootroot"
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    DEFAULT_EXPIRATION_TOKEN = 15


    ## Files Kind

    BACKGROUND = 1
    GRADES = 2
    TRANSFERRED_GRADES = 3
    COURSE_INFO = 4
    AID = 5
    MAIN = 6



settings = Settings()
