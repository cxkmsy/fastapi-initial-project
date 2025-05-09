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

