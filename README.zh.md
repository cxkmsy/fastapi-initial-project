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
1. 项目管理
   
- 添加项目
通过 POST 请求 /projects 接口添加新项目。

{
    "title": "New Project",
    "user_id": 1
}
【这里是添加项目的截图】
![添加项目截图]()

- 获取所有项目
通过 GET 请求 /projects 接口获取所有项目。
【这里是获取所有项目的截图】
![获取所有项目截图]()

1. 用户管理
   
- 用户注册
通过 POST 请求 /users 接口注册新用户。

{
    "name": "  ",
    "email": "  ",
    "password": "  "
}
【这里是用户注册的截图】
![用户注册截图]()

- 用户登录
  通过 POST 请求 /users/login 接口进行用户登录。

{
    "username": "johndoe@example.com",
    "password": "password123"
}

  【这里是获取所有项目的截图】
  ![获取所有项目截图]()