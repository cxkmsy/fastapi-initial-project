from app.routers import users, projects


def load_routes(app):
    app.include_router(users.router)
    app.include_router(projects.router)
