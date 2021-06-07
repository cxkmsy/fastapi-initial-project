import uvicorn
from app import config

from fastapi import Depends, FastAPI, HTTPException, status, Response
from app.routers import users as userRoute
from app.schemas import schema

app = FastAPI()
schema.index()
app.include_router(userRoute.router)


if __name__ == "__main__":
    uvicorn.run(app, host=config.settings.HOST, port=config.settings.PORT)
