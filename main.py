import uvicorn
from app import config

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import index as indexRoute
from app.schemas import schema

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
schema.index()
indexRoute.load_routes(app)



if __name__ == "__main__":
    uvicorn.run(app, host=config.settings.HOST, port=config.settings.PORT)
