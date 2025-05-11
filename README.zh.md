FastApi 最佳实践模式
带有身份验证和错误处理的 FastApi 框架最佳面向对象模式
创建一个虚拟环境，然后运行 pip install -r requirements.txt 安装依赖项。
创建一个空数据库（项目中的默认名称为 test_db）。
根据你的 MySQL 凭证修改 app/config.py。
在命令行中运行 uvicorn main:app --reload。
在浏览器中打开 http://127.0.0.1:8000/docs。

FastAPI 模型模块(models（作者：班庭锐 2205308010349）
该模块定义了 FastAPI 项目中使用的核心数据模型，涵盖了与项目和用户相关的数据结构。

✨ 特性
清晰的模型定义：利用 Pydantic 库精确地定义项目和用户的数据结构。
支持创建和更新操作：提供用于创建和更新项目及用户的模型。
ORM 模式兼容性：数据模型支持 ORM 模式，实现与数据库的高效交互。

📦 项目结构
fastapi-initial-project/
└── app/
└── models/
├── **init**.py # 初始化文件
├── projects.py # 与项目相关的数据模型
└── users.py # 与用户相关的数据模型

📮 核心模型解析（作者：班庭锐）
一、项目模型（projects.py）
基础项目信息模型（ProjectBase）
定义项目的基础字段，作为其他模型的基类：
from pydantic import BaseModel
class ProjectBase(BaseModel):
title: str

项目创建模型（ProjectCreate）
继承自 ProjectBase，并添加 user_id 字段（必填），用于指定创建项目的用户 ID：
class ProjectCreate(ProjectBase):
user_id: int

项目更新模型（ProjectUpdate）
继承自 ProjectBase，字段设置为可选，以支持部分更新：
from typing import Optional
class ProjectUpdate(ProjectBase):
title: Optional[str] = None

完整项目信息模型（Project）
继承自 ProjectBase，添加数据库字段（ID、user_id），并启用 ORM 模式：
class Project(ProjectBase):
id: int
user_id: int
class Config:
orm_mode = True # 支持从 SQLAlchemy 模型转换

二、用户模型（users.py）
基础用户信息模型（UserBase）
定义用户的基础字段（姓名、邮箱、激活状态）：
class UserBase(BaseModel):
name: str
email: str
is_active: bool

用户创建模型（UserCreate）
继承自 UserBase，并添加 password 字段（用户注册时必填）：
class UserCreate(UserBase):
password: str

用户更新模型（UserUpdate）
继承自 UserBase，所有字段设置为可选，以支持部分更新：
class UserUpdate(UserBase):
name: Optional[str] = None
email: Optional[str] = None
password: Optional[str] = None
is_active: Optional[bool] = None

完整用户信息模型（User）
继承自 UserBase，添加用户 ID，并启用 ORM 模式：
class User(UserBase):
id: int
class Config:
orm_mode = True

用户登录模型（UserLogin）
用于用户认证，包含邮箱和密码字段（登录时进行验证）：
class UserLogin(BaseModel):
email: str
password: str
class Config:
orm_mode = True

令牌模型（Token）
表示用户登录后返回的令牌结构（访问令牌、令牌类型）：
class Token(BaseModel):
access_token: str
token_type: str
class Config:
orm_mode = True

令牌数据模型（TokenData）
用于存储令牌中的数据，目前仅包含用户的邮箱（可选）：
from typing import Optional
class TokenData(BaseModel):
email: Optional[str] = None
（作者：班庭锐 2205308010349）