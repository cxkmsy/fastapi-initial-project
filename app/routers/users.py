from typing import List
from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from app import database
from app.controllers import users as userController
from app.models import users as userModel
from fastapi.security import OAuth2PasswordRequestForm
from app.middlewares import auth

router = APIRouter(
    tags=['Users'],
    prefix="/user")


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[userModel.User])
def get_all(db: Session = Depends(database.get_db), current_user: auth.User = Depends(auth.get_current_user)):
    return userController.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=userModel.User)
def create(request: userModel.UserCreate, db: Session = Depends(database.get_db)):
    return userController.create(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=userModel.User)
def get_one(id: int, db: Session = Depends(database.get_db), current_user: auth.User = Depends(auth.get_current_user)):
    return userController.get_one(db, id)


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=userModel.User)
def update(id: int, request: userModel.UserUpdate, db: Session = Depends(database.get_db), current_user: auth.User = Depends(auth.get_current_user)):
    return userController.update(db, request, id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db), current_user: auth.User = Depends(auth.get_current_user)):
    return userController.destroy(db, id)


@router.post("/login", status_code=status.HTTP_200_OK, response_model=userModel.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: Session = Depends(database.get_db)):
    return userController.login(form_data, db)
