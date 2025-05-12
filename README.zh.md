
<!--------------------------------------------- by2205308010333徐济艺 ------------------------------------------------------------->

# FastAPI 初始项目 - 控制器模块介绍

本项目是一个基于 FastAPI 的初始项目，控制器模块（controllers）主要负责处理业务逻辑，包括项目（projects）和用户（users）相关的操作。

## ✨ 项目特点

- 提供项目和用户的增删改查操作。
- 对数据库操作进行异常处理，提高系统稳定性。
- 支持用户登录和 JWT 令牌验证

## 🚀 快速开始

### 克隆项目

git clone [你的项目仓库地址]
cd [项目文件夹名]

### 安装依赖

pip install -r requirements.txt

### 启动项目

uvicorn main:app --reload

项目将运行在 http://localhost:8000

## 📦 项目结构
fastapi-initial-project-master/
├── app/
│   ├── controllers/
│   │   ├── projects.py  # 项目相关控制器
│   │   └── users.py     # 用户相关控制器
│   ├── helpers/
│   ├── middlewares/
│   ├── models/
│   ├── routers/
│   └── schemas/
└── ...

## 📮 项目主要功能说明与截图
一、用户管理功能（对应users.py）

- 用户注册(create 函数)
  功能对应：接收用户注册请求，加密密码后存入数据库。

![用户注册代码截图](images/1.png)


- 用户登录（login 函数）
  功能对应：验证用户邮箱和密码，生成并返回 JWT 认证令牌。

![用户登录代码截图](images/2.png)

- 查询单个用户（get_one 函数）
  功能对应：根据用户 ID 查询用户详情，未找到时返回 404 错误。

![查询单个用户代码截图](images/3.png)

- 更新用户信息（update 函数）
  功能对应：支持更新用户信息（包括密码，自动加密），未找到用户时返回 404 错误。
  ![更新用户信息代码截图](images/4.png)

- 删除用户（destroy 函数）
  功能对应：根据用户 ID 删除用户，未找到时返回 404 错误。
  ![删除用户代码截图](images/5.png)

  二、项目管理功能（对应 projects.py）

- 创建项目（create 函数）
  功能对应：创建新项目，强制关联 user_id（确保每个项目属于特定用户）。
  ![创建项目代码截图](images/6.png)

- 查询所有项目（get_all 函数）
  功能对应：返回数据库中所有项目记录（实际使用时可能需结合用户 ID 过滤，当前代码未体现，可在文档中说明 “需结合认证逻辑过滤当前用户的项目”）。
  ![查询所有项目代码截图](images/7.png)

- 查询单个项目（get_one 函数）
  功能对应：根据项目 ID 查询详情，未找到时返回 404 错误。
  ![查询单个项目代码截图](images/8.png)

- 更新项目（update 函数）
  功能对应：根据项目 ID 更新信息，未找到时返回 404 错误。
  ![更新项目代码截图](images/9.png)

- 删除项目（destroy 函数）
  功能对应：根据项目 ID 删除项目，未找到时返回 404 错误。
  ![删除项目代码截图](images/10.png)

三、认证机制（对应 users.py）

- JWT 令牌生成（create_access_token 函数）
  功能对应：生成带有过期时间的 JWT 令牌，用于用户认证。
  ![JWT 令牌生成代码截图](images/11.png)

- JWT 令牌验证（verify_token 函数）
  功能对应：验证 JWT 令牌的有效性，提取用户邮箱用于权限验证。
  ![JWT 令牌验证代码截图](images/12.png)
  <!--------------------------------------------- by2205308010333徐济艺 ------------------------------------------------------------->
=======

#2205308010313 李念毅
# FastApi_best_practice_pattern

### Best Object-Oriented pattern for FastApi framework with Authentication and error handling  

- Create a Virtual Environment and run `pip install -r requirements.txt` to install the dependencies.
- Create an empty database (default name in the project is `test_db`).
- Change the app/config.py based on your MySql credential.
- Run `uvicorn main:app --reload` in command line.
- Open `http://127.0.0.1:8000/docs` in the browser.

# FastAPI 项目路由模块

本模块包含项目的主要API路由定义，包括用户管理和项目管理功能。

## 🚀 功能特性

- 👥 完整的用户认证系统（登录/注册）
- 🔐 基于JWT的权限控制
- 📦 项目管理CRUD操作
- 🛡️ 路由级权限校验

## 📂 文件结构
router/
├── init.py # 包初始化文件
├── index.py # 路由加载入口
├── projects.py # 项目相关路由
└── users.py # 


## 🛠️ 路由说明
![项目界面截图](images/users3.png)
### 用户路由 (/user)
- `GET /user` - 获取所有用户列表 (需认证)
- `POST /user` - 创建新用户
- `GET /user/{id}` - 获取指定用户详情 (需认证)
- `PUT /user/{id}` - 更新用户信息 (需认证)
- `DELETE /user/{id}` - 删除用户 (需认证)
- `POST /user/login` - 用户登录 (获取访问令牌)

![项目界面截图](images/projects3.png)
### 项目路由 (/project)
- `GET /project` - 获取所有项目列表 (需认证)
- `POST /project` - 创建新项目 (需认证)
- `GET /project/{id}` - 获取指定项目详情 (需认证)
- `PUT /project/{id}` - 更新项目信息 (需认证)
- `DELETE /project/{id}` - 删除项目 (需认证)

## � 开发指南

1. 添加新路由文件时，需在`index.py`中注册
2. 使用`APIRouter`的`dependencies`参数添加路由级中间件
3. 响应模型统一使用`app.models`中定义的模型
#2205308010313 李念毅

<!-- by wenliangfeng -->

# 克隆项目:
git clone https://github.com/wenliangfeng/fastapi-initial-project.git
cd fastapi-initial-project


app/helpers/ 目录下的认证系统模块，提供安全的用户认证功能，包含：
JWT令牌生成与验证 (auth.py)
密码哈希加密与验证 (hashing.py)
✅ 功能特点:
基于 JWT 的无状态认证
使用 Bcrypt 的安全密码哈希
可配置的令牌过期时间
自动加盐的密码加密

# 安装依赖:
pip install python-jose[cryptography] passlib bcrypt

# 配置环境变量
在 .env 文件中添加：

SECRET_KEY=your_random_secret_key_here
ALGORITHM=HS256
DEFAULT_EXPIRATION_TOKEN=30  # 单位：分钟

# 核心功能调用:
python
from app.helpers.auth import create_access_token, decode_token
from app.helpers.hashing import get_password_hash, verify_password
from datetime import timedelta

# 生成令牌
token = create_access_token(
    data={"user_id": 123},
    expires_delta=timedelta(hours=2)
)

# 密码加密与验证
hashed_pw = get_password_hash("mypassword")
verify_password("mypassword", hashed_pw)  # 返回 True/False

🏗️ 项目结构
app/
└── helpers/
    ├── auth.py           # JWT认证核心逻辑
    ├── hashing.py        # 密码哈希处理
    └── __init__.py       # 模块导出

# 功能截图：

生成访问令牌：images/token_flow.png
密码验证流程：images/password_flow.png

📚 技术栈说明
技术	用途	版本要求
python-jose	JWT实现	>=3.3.0
passlib	密码哈希	>=1.7.4
bcrypt	哈希算法	>=4.0.1


# 安全规范

# 密码安全策略
# 密码强度要求示例
def validate_password(password):
    return (
        len(password) >= 8 and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password)
    )

 <!-- by wenliangfeng -->


<--! 黄成臻 -->
### README.zh.md
# FATSAPI 项目

### 🇨🇳 中文版

## ✨ 项目特点

- 🏗️ 采用面向对象设计模式
- 🔐 集成JWT认证系统
- 🛡️ 完善的错误处理机制
- 🗃️ MySQL数据库支持
- 📝 自动API文档生成(Swagger UI)

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/cxkmsy/fastapi-initial-project.git
cd fastapi-initial-project-master
```

### 2. 创建虚拟环境并安装依赖
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3. 数据库配置
修改 `app/config.py` 中的数据库连接信息：
```python
DB_HOST: str = "localhost"     # 数据库主机地址
DB_PORT: str = "3306"          # 数据库端口
DB_NAME: str = "test_db"       # 数据库名称
DB_USER: str = "root"          # 数据库用户名
DB_PASS: str = "rootroot"      # 数据库密码
```

### 4. 启动项目
```bash
uvicorn main:app --reload
```

访问 `http://127.0.0.1:8000/docs` 查看API文档

## ⚙️ 核心配置

### 认证配置
```python
SECRET_KEY = "09d25e094faa..."  # JWT加密密钥
ALGORITHM = "HS256"            # 加密算法
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # 访问令牌过期时间
```

### 数据库连接
采用SQLAlchemy ORM，连接配置位于 `app/database.py`：
```python
# MySQL连接字符串格式
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://用户:密码@主机:端口/数据库名称?charset=utf8mb4"

# 数据库会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

## 📦 项目结构
```
fastapi-project/
├── app/
│   ├── controllers/          # 业务逻辑处理
│   │   ├── __init__.py
│   │   ├── projects.py
│   │   └── users.py
│   ├── helpers/             # 辅助工具
│   │   ├── __init__.py
│   │   ├── auth.py          # 认证辅助
│   │   └── hashing.py       # 加密相关
│   ├── middlewares/         # 中间件
│   │   ├── __init__.py
│   │   └── auth.py          # 认证中间件
│   ├── models/              # 数据模型
│   │   ├── __init__.py
│   │   ├── projects.py
│   │   └── users.py
│   ├── routers/             # API路由
│   │   ├── __init__.py
│   │   ├── index.py         # 根路由
│   │   ├── projects.py
│   │   └── users.py
│   ├── schemas/             # Pydantic模型
│   │   ├── __init__.py
│   │   ├── projects.py
│   │   ├── schema.py        # 基础模型
│   │   └── users.py
│   ├── __init__.py          # 应用初始化
│   ├── config.py            # 配置文件
│   └── database.py          # 数据库连接
├── tests/                   # 测试用例
├── venv/                    # 虚拟环境
├── .gitignore
├── LICENSE
├── main.py                  # 应用入口
├── README.md
└── requirements.txt         # 依赖列表
```
<--! by 黄成臻 -->


<!--by bantingrui 2205308010349-->
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
<!--by bantingrui 2205308010349-->


<!--张振锟-->
# FastAPI 初始项目

## 简介

这是一个基于 [FastAPI](https://fastapi.tiangolo.com/) 框架的初始项目模板，旨在帮助开发者快速启动基于 Python 的 Web 应用程序。该项目采用模块化设计，支持快速开发、扩展和部署。

---

## 功能特性

- 🚀 **快速启动**：包含最小化的 FastAPI 项目结构。
- 🛠️ **可扩展**：模块化代码结构，易于扩展新功能。
- 📦 **依赖管理**：使用 `requirements.txt` 或 `poetry` 管理依赖。
- 🔐 **安全性**：内置支持环境变量管理（`.env` 文件）。
- 🗃️ **数据库支持**：支持多种数据库（如 SQLite、PostgreSQL）。
- 🌐 **API 文档**：自动生成交互式 API 文档（Swagger UI 和 ReDoc）。

---

## 环境要求

在开始之前，请确保您的开发环境满足以下要求：

- Python 版本：`>=3.8`
- 推荐操作系统：Windows、MacOS、Linux
- 包管理工具：`pip` 或 `poetry`

---

## 安装步骤

### 1. 克隆项目代码

```bash
git clone https://github.com/zzk-zuishuai/fastapi-initial-project.git
cd fastapi-initial-project
```

### 2. 创建虚拟环境

使用 `venv` 创建虚拟环境并激活：

```bash
python -m venv venv
# 激活虚拟环境 (Linux/MacOS)
source venv/bin/activate
# 激活虚拟环境 (Windows)
venv\Scripts\activate
```

### 3. 安装项目依赖

```bash
pip install -r requirements.txt
```

---

## 使用说明

### 运行开发服务器

在开发模式下运行服务器：

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

服务器启动后，您可以访问以下地址：

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 数据库迁移

如果项目使用了数据库，请确保运行迁移脚本：

```bash
alembic upgrade head
```

---

## 部署指南

以下是生产环境的部署步骤示例：

### 1. 使用 Gunicorn 部署

```bash
gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
```

### 2. 配置 Nginx 反向代理

以下是 Nginx 配置示例：

```nginx
server {
    listen 80;
    server_name your_domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 3. 使用 Docker 部署（可选）

创建一个 `Dockerfile`：

```dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

构建并运行 Docker 镜像：

```bash
docker build -t fastapi-app .
docker run -d -p 8000:8000 fastapi-app
```

---

## 目录结构

以下是项目的主要目录结构：

```plaintext
fastapi-initial-project/
├── app/
│   ├── main.py          # FastAPI 应用入口
│   ├── routers/         # 路由模块
│   ├── models/          # 数据模型
│   ├── schemas/         # 数据验证模型
│   └── utils/           # 工具函数
├── tests/               # 测试代码
├── requirements.txt     # 项目依赖
├── Dockerfile           # Docker 配置
└── README.md            # 项目说明文档
```
<!--张振锟-->

<!-- by 2205308010338蒙思勇 -->
# FATSAPI 项目

这是一个基于 "FastAPI" 和 "Vue.js" 的任务管理工具，旨在帮助用户高效地管理任务。项目适合用来学习和实践全栈开发，尤其是 FastAPI 和 Vue.js 的结合使用。

## ✨ 项目特点

- 📝 "任务管理"：支持添加、编辑、删除任务，帮助用户清晰地规划和管理日常任务。
- ✅ "任务状态管理"：可以勾选任务为已完成状态，方便用户跟踪任务进度。
- 💾 "数据存储"：
  - 前端：支持浏览器 LocalStorage 存储任务数据，便于快速体验。
  - 后端：使用数据库（如 MySQL）存储任务数据，确保数据持久化。
- 🎨 "响应式设计" ：界面适配手机和 PC，提供良好的用户体验。
- 🔗 "API 支持"  ：后端提供 RESTful API，方便与其他系统集成。

## 🚀 快速开始

### 克隆项目

```bash
https://github.com/cxkmsy/fastapi-initial-project.git
cd fastapi-initial-project
```

### 后端部分

1. **安装依赖**：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

2. **配置数据库**：
   - 确保 MySQL 或其他数据库已安装并运行。
   - 修改 `app/config.py` 文件中的数据库配置。

3. **初始化数据库**：
   ```bash
   python -c "from app.schemas.schema import index; index()"
   ```

4. **运行后端服务**：
   ```bash
   uvicorn app.main:app --reload
   ```
   后端服务将运行在 `http://127.0.0.1:8000`。

### 前端部分

1. **安装依赖**：
   ```bash
   cd frontend
   npm install
   ```

2. **启动前端服务**：
   ```bash
   npm run dev
   ```
   前端服务将运行在 `http://localhost:5173`。

## 📮 API 文档

后端提供了自动生成的 API 文档，可以通过以下地址访问：
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`


## 📦 项目结构

```
fastapi-initial-project/
├── app/                  # 后端代码目录
│   ├── controllers/      # 控制器模块，处理业务逻辑
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── projects.py   # 项目相关的业务逻辑
│   │   ├── users.py      # 用户相关的业务逻辑
│   ├── helpers/          # 辅助工具模块
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── auth.py       # 认证相关的工具函数
│   │   ├── hashing.py    # 哈希处理工具（如密码加密）
│   ├── middlewares/      # 中间件模块
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── auth.py       # 认证中间件
│   ├── models/           # 数据库模型定义
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── projects.py   # 项目模型
│   │   ├── users.py      # 用户模型
│   ├── routers/          # 路由模块
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── index.py      # 路由加载入口
│   │   ├── projects.py   # 项目相关的路由
│   │   ├── users.py      # 用户相关的路由
│   ├── schemas/          # 数据验证和序列化模块
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── projects.py   # 项目相关的 Pydantic 模型
│   │   ├── schema.py     # 数据库初始化脚本
│   │   ├── users.py      # 用户相关的 Pydantic 模型
│   ├── __init__.py       # 包初始化文件
│   ├── config.py         # 配置文件（如数据库连接配置）
│   ├── database.py       # 数据库连接和初始化
│
├── .gitignore            # Git 忽略文件配置
├── LICENSE               # 项目许可证
├── main.py               # FastAPI 应用主入口
├── README.md             # 英文版项目说明文档
├── README.zh.md          # 中文版项目说明文档
├── requirements.txt      # Python 依赖列表
├── terms.md              # 项目条款或说明
├── ai_usage_screenshots  # AI 使用截图目录
```

## 📸 项目功能与截图

### 1. 添加任务
用户可以通过输入任务名称和描述来添加新任务。

![添加任务界面]

### 2. 查看任务列表
任务列表展示所有任务，包括未完成和已完成的任务。

![任务列表界面]

### 3. 编辑任务
支持对已有任务进行修改，包括任务名称和描述。

![编辑任务界面]

### 4. 删除任务
用户可以删除不需要的任务。

![删除任务界面]

### 5. 勾选已完成任务
通过勾选任务，标记任务为已完成状态。

![勾选任务界面]

<!-- by 2205308010338蒙思勇 -->

