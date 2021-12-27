from app.schemas import users, projects

from app.database import engine


def index():
    users.Base.metadata.create_all(engine)
    projects.Base.metadata.create_all(engine)

