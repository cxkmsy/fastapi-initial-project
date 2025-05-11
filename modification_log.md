 <!--------------------------------------------- by2205308010333徐济艺------------------------------------------------------------>

一、审查了controllers中projects.py文件代码的结构，存在几个需要注意的问题：
1. 变量名不一致
在 get_one() 函数中，查询的是 Project 对象，但返回的变量名是 user，这会导致语义混淆。
2. 潜在的事务管理问题
在 update() 和 destroy() 函数中，如果发生错误，没有显式回滚事务。虽然 SQLAlchemy 通常会自动回滚，但在复杂场景下可能出现问题。
3. 异常处理不完善
所有数据库操作都捕获了 SQLAlchemyError，但对于非数据库相关的错误（如请求参数解析错误）没有处理。
4. 响应格式不一致
destroy() 函数返回 Response(status_code=204)，而其他函数返回对象实例，可能导致前端处理不一致。
5. 缺少类型注解
create() 和 update() 函数的 request 参数缺少类型注解，降低了代码的可读性和 IDE 的自动补全功能。
修正后的代码：from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.schemas.projects import Project
from app.models.projects import Project as DBProject  # 假设数据库模型名称为 Project


def get_all(db: Session) -> list[DBProject]:
    try:
        result = db.query(DBProject).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def create(request: Project, db: Session) -> DBProject:
    new_item = DBProject(
        title=request.title,
        user_id=request.user_id
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        db.rollback()  # 显式回滚
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def get_one(db: Session, item_id: int) -> DBProject:
    try:
        project = db.query(DBProject).filter(DBProject.id == item_id).first()
        if not project:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return project


def update(db: Session, request: Project, item_id: int) -> DBProject:
    try:
        project = db.query(DBProject).filter(DBProject.id == item_id)
        if not project.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        
        update_data = request.dict(exclude_unset=True)
        project.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()  # 显式回滚
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    
    return project.first()


def destroy(db: Session, item_id: int) -> Response:
    try:
        project = db.query(DBProject).filter(DBProject.id == item_id)
        if not project.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        
        project.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()  # 显式回滚
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
 <!--------------------------------------------- by2205308010333徐济艺------------------------------------------------------------>

二、审查了controllers中users.py文件代码的结构，存在几个需要注意的问题：
1. 缺少类型注解
create、update、login 等函数的 request 参数缺少类型注解，降低了代码的可读性和 IDE 的自动补全功能。
2. 变量名不一致
在 login 函数中，request 参数是 OAuth2PasswordRequestForm 类型，但直接使用 request.username 和 request.password，可能导致混淆（通常应为 form_data.username 和 form_data.password）。
3. 验证逻辑不完整
verify_token 函数解析 token 后没有返回用户信息，导致无法在依赖项中获取当前用户。
4. 缺少用户依赖项
没有提供获取当前登录用户的依赖函数，无法在需要权限验证的路由中使用。
5. 异常处理不完善
所有数据库操作都捕获了 SQLAlchemyError，但对于非数据库相关的错误（如 JWT 解析错误）没有统一处理。
密码哈希验证可能存在问题
假设 hashing.verify_password 函数正确实现，但需要确认其内部逻辑是否正确。
下面是修正后的代码：from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException, status, Response, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from jose import JWTError, jwt

from app.helpers import hashing
from app.schemas.users import User as UserSchema
from app.models.users import User as DBUser  # 假设数据库模型名称为 User

from app import config

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")


def get_all(db: Session) -> list[DBUser]:
    try:
        result = db.query(DBUser).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def create(request: UserSchema, db: Session) -> DBUser:
    try:
        hashed_password = hashing.get_password_hash(request.password)
        new_user = DBUser(name=request.name, email=request.email, password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except SQLAlchemyError as e:
        db.rollback()  # 显式回滚
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_user


def get_one(db: Session, user_id: int) -> DBUser:
    try:
        user = db.query(DBUser).filter(DBUser.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return user


def update(db: Session, request: UserSchema, user_id: int) -> DBUser:
    try:
        user = db.query(DBUser).filter(DBUser.id == user_id)
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
        
        update_data = request.dict(exclude_unset=True)
        set_password = update_data.get("password")
        if set_password:
            update_data["password"] = hashing.get_password_hash(set_password)
        
        user.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()  # 显式回滚
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    
    return user.first()


def destroy(db: Session, user_id: int) -> Response:
    try:
        user = db.query(DBUser).filter(DBUser.id == user_id)
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
        
        user.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()  # 显式回滚
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends()) -> dict:
    user = db.query(DBUser).filter(DBUser.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found!")
    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Your Password is incorrect!")
    
    access_token_expires = timedelta(minutes=config.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "id": user.id},  # 添加用户 ID 到 token 中
        expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, 
        config.settings.SECRET_KEY, 
        algorithm=config.settings.ALGORITHM
    )
    return encoded_jwt


def verify_token(token: str, credentials_exception) -> dict:
    try:
        payload = jwt.decode(
            token, 
            config.settings.SECRET_KEY, 
            algorithms=[config.settings.ALGORITHM]
        )
        email: str = payload.get("sub")
        user_id: int = payload.get("id")
        
        if email is None or user_id is None:
            raise credentials_exception
        
        return {"email": email, "id": user_id}
    except JWTError:
        raise credentials_exception


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends()) -> DBUser:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    token_data = verify_token(token, credentials_exception)
    user = get_one(db, token_data["id"])
    
    if user is None:
        raise credentials_exception
    
    return user
 <!--------------------------------------------- by2205308010333徐济艺------------------------------------------------------------>
