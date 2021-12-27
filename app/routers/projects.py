from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from app import database
from app.controllers import projects as controller
from app.models import projects as model
from app.middlewares import auth

router = APIRouter(
    tags=['Project'],
    prefix="/project",
    dependencies=[Depends(auth.get_current_user)]
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[model.Project])
def get_all(db: Session = Depends(database.get_db)):
    return controller.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=model.Project)
def create(request: model.ProjectCreate, db: Session = Depends(database.get_db)):
    return controller.create(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=model.Project)
def get_one(id: int, db: Session = Depends(database.get_db)):
    return controller.get_one(db, id)


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=model.Project)
def update(id: int, request: model.ProjectUpdate, db: Session = Depends(database.get_db)):
    return controller.update(db, request, id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db)):
    return controller.destroy(db, id)
