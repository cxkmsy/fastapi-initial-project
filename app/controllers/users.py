from fastapi import Depends, FastAPI, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.schemas.users import User
from app.helpers import hashing


def get_all(db: Session):
    return db.query(User).all()


def create(request, db: Session):
    hashed_password = hashing.bcrypt(request.password)
    new_user = User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_one(db: Session, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    return user


def update(db: Session, request, user_id):
    updated = db.query(User).filter(User.id == user_id)
    if not updated.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    update_data = request.dict(exclude_unset=True)
    set_password = update_data.get("password")
    if set_password:
        update_data["password"] = hashing.bcrypt(set_password)
    updated.update(update_data, synchronize_session=False)
    db.commit()
    return updated.first()


def destroy(db: Session, user_id):
    data = db.query(User).filter(User.id == user_id)
    if not data.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    data.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
