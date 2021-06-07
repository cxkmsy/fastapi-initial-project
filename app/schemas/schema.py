from app.schemas import users
from app.database import engine


def index():
    users.Base.metadata.create_all(engine)
