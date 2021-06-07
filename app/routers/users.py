from typing import List
from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from app import database
from app.controllers import users as userController
from app.models import users as userModel

router = APIRouter(
    tags=['Users'],
    prefix="/user")


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[userModel.User])
def get_all(db: Session = Depends(database.get_db)):
    return userController.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=userModel.User)
def create(request: userModel.UserCreate, db: Session = Depends(database.get_db)):
    return userController.create(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=userModel.User)
def get_one(id: int, db: Session = Depends(database.get_db)):
    return userController.get_one(db, id)


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=userModel.User)
def update(id: int, request: userModel.UserUpdate, db: Session = Depends(database.get_db)):
    return userController.update(db, request, id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db)):
    return userController.destroy(db, id)
