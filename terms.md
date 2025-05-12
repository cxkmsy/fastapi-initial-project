
<!--------------------------------------------- by2205308010333徐济艺 ------------------------------------------------------------->
1. FastAPI
- 定义：一个基于 Python 的现代高性能 Web 框架，用于快速构建 API，支持异步编程、自动生成交互式文档（Swagger/OpenAPI）和严格的类型提示。
项目应用：本项目基于 FastAPI 搭建，控制器模块（controllers）通过 FastAPI 的依赖注入和路由系统，实现对用户和项目资源的 RESTful 接口管理。
2. SQLAlchemy
- 定义：Python 中流行的 SQL 工具包和对象关系映射器（ORM），允许通过 Python 类操作数据库，将数据库表映射为对象，简化数据库交互逻辑。
项目应用：在 projects.py 和 users.py 中，通过 SQLAlchemy 的会话（Session）对象执行数据库查询（如 db.query(Project).all()），实现对项目和用户数据的增删改查操作，并处理数据库异常（如 SQLAlchemyError）。
3. JWT（JSON Web Token）
- 定义：一种开放标准（RFC 7519），用于在网络应用间安全传输信息的令牌，通常用于用户认证和授权，包含用户信息和过期时间等数据，通过签名确保不可篡改。
项目应用：在 users.py 的登录逻辑中，生成 JWT 令牌（create_access_token）并返回给客户端，后续请求通过令牌验证用户身份（verify_token），实现无状态认证。
4. 控制器（Controller）
- 定义：在 MVC（模型 - 视图 - 控制器）架构中，控制器是处理用户请求、协调模型和视图的中间层，负责接收输入、调用业务逻辑并返回响应。
项目应用：controllers 目录下的 projects.py 和 users.py 分别封装了项目和用户相关的业务逻辑，如数据验证、数据库操作和异常处理，是连接路由（routers）和模型（models）的核心模块。
5. ORM（对象关系映射）
- 定义：一种编程技术，将数据库中的表映射为编程语言中的对象，通过操作对象实现对数据库的增删改查，避免直接编写 SQL 语句，提高开发效率和代码可维护性。
项目应用：本项目通过 SQLAlchemy 的 ORM 模型（如 Project 和 User 类）定义数据库表结构，控制器中的方法（如 get_all、create）通过操作这些对象完成数据库交互，例如 db.add(new_item) 对应插入数据库记录。
6. 依赖注入（Dependency Injection）
- 定义：一种设计模式，通过将依赖（如数据库会话、配置对象）传递给函数或类，而非硬编码，提高代码的松耦合性和可测试性。
项目应用：FastAPI 原生支持依赖注入，控制器函数（如 get_all(db: Session)）通过参数声明依赖（如 db: Session），框架会自动解析并注入数据库会话，简化资源管理。

1. FastAPI
- Definition: A modern, high-performance Python-based Web framework for rapidly building APIs. It supports asynchronous programming, automatic generation of interactive documentation (Swagger/OpenAPI), and strict type hints.
Project application: This project is built on FastAPI. The controller module (controllers) uses FastAPI's dependency injection and routing system to implement RESTful interface management for user and project resources.
2. SQLAlchemy
- Definition: A popular SQL toolkit and object-relational mapper (ORM) in Python. It allows database operations through Python classes by mapping database tables to objects, simplifying database interaction logic.
Project application: In projects.py and users.py, database queries (e.g., db.query(Project).all()) are executed through SQLAlchemy's session (Session) object to perform create, read, update, and delete operations on project and user data and handle database exceptions (e.g., SQLAlchemyError).
3. JWT (JSON Web Token)
- Definition: An open standard (RFC 7519) for securely transmitting information between web applications. It is commonly used for user authentication and authorization, containing user information and expiration time. The token is signed to ensure its integrity.
Project application: In the login logic of users.py, a JWT token (create_access_token) is generated and returned to the client. Subsequent requests verify the user's identity through the token (verify_token) to achieve stateless authentication.
4. Controller
- Definition: In the MVC (Model - View - Controller) architecture, the controller is an intermediate layer that handles user requests, coordinates the model and the view. It is responsible for receiving input, invoking business logic, and returning responses.
Project application: projects.py and users.py in the controllers directory encapsulate business logic related to projects and users, such as data validation, database operations, and exception handling. They are the core modules connecting the routers and the models.
5. ORM (Object-Relational Mapping)
- Definition: A programming technique that maps database tables to objects in a programming language. It enables create, read, update, and delete operations on the database by manipulating objects, eliminating the need to write SQL statements directly, thus improving development efficiency and code maintainability.
Project application: In this project, the database table structure is defined through SQLAlchemy's ORM models (e.g., Project and User classes). Methods in the controller (e.g., get_all, create) perform database interactions by manipulating these objects. For example, db.add(new_item) corresponds to inserting a record into the database.
6. Dependency Injection
- Definition: A design pattern that passes dependencies (e.g., database sessions, configuration objects) to functions or classes instead of hard - coding them, improving code decoupling and testability.
Project application: FastAPI natively supports dependency injection. Controller functions (e.g., get_all(db: Session)) declare dependencies (e.g., db: Session) through parameters, and the framework automatically resolves and injects the database session, simplifying resource management.
<!--------------------------------------------- by2205308010333徐济艺 ------------------------------------------------------------->
=======

#2205308010313 李念毅
# 术语词汇表 | Glossary

| 中文术语 | English Term | 说明 / Description |
|----------|--------------|--------------------|
| 路由 | Route | API端点路径定义 / API endpoint path definition |
| 认证 | Authentication | 验证用户身份的过程 / Process of verifying user identity |
| 授权 | Authorization | 确定用户权限的过程 / Process of determining user permissions |
| 中间件 | Middleware | 处理请求和响应的组件 / Component that processes requests and responses |
| 响应模型 | Response Model | 定义API返回数据结构的模型 / Model defining API response structure |
| 依赖注入 | Dependency Injection | 自动解析和注入依赖项的设计模式 / Design pattern for automatic dependency resolution |
| CRUD操作 | CRUD Operations | 创建、读取、更新、删除基本操作 / Create, Read, Update, Delete basic operations |
| JWT令牌 | JWT Token | JSON Web Token用于安全传输信息 / JSON Web Token for secure information transfer |
#2205308010313 李念毅

<!-- by wenliangfeng -->
| 英文术语 | 中文翻译 | 定义说明 |
|---------|---------|---------|
| JWT (JSON Web Token) | JSON网络令牌 | RFC 7519标准的加密令牌格式，用于安全传输声明 |
| Bcrypt | 跨平台哈希算法 | 专为密码存储设计的自适应哈希算法 |
| CryptContext | 加密上下文 | Passlib库提供的密码策略管理器 |
| OAuth2PasswordBearer | OAuth2密码承载 | FastAPI实现的密码模式认证方案 |
| Payload | 有效载荷 | JWT中存储的实际数据部分 |
| Secret Key | 密钥 | 用于签名/验证令牌的加密密钥 |
| HS256 (HMAC-SHA256) | 哈希消息认证码 | JWT常用签名算法 |
| LocalStorage | 本地存储 | 浏览器端数据存储方案 |
| Token Expiration | 令牌有效期 | JWT令牌的有效时间周期 |
| Salt | 盐值 | 密码哈希过程中添加的随机数据 |
| Stateless Authentication | 无状态认证 | 不依赖服务端会话的认证机制 |
# 安全扩展术语
| 英文术语 | 中文翻译 | 应用场景 |
|---------|---------|---------|
| Refresh Token | 刷新令牌 | 用于获取新访问令牌 |
| CSRF Protection | CSRF防护 | 防止跨站请求伪造 |
| CORS | 跨域资源共享 | API跨域访问控制 |
| PBKDF2 | 密码派生函数 | 替代Bcrypt的算法 |
| Rate Limiting | 速率限制 | 防止暴力破解 |

<!-- by wenliangfeng -->


<--! 黄成臻 -->
面向对象设计模式 / Object-Oriented design pattern

JWT认证系统 / JWT Authentication system

完善的错误处理机制 / Comprehensive error handling

MySQL数据库支持 / MySQL database support

自动API文档生成 / Automatic API documentation

克隆项目 / Clone the repository

创建虚拟环境 / Create virtual environment

安装依赖 / Install dependencies

数据库配置 / Database configuration

启动项目 / Run the application

认证配置 / Authentication

数据库连接 / Database Connection

JWT加密密钥 / JWT secret key

加密算法 / Encryption algorithm

访问令牌过期时间 / Token expiration time

业务逻辑处理 / Business logic handlers

辅助工具 / Utility helpers

中间件 / Middleware components

数据模型 / Database models

API路由 / API routers

Pydantic模型 / Pydantic schemas

应用入口 / Application entry point

虚拟环境 / Virtual environment

依赖列表 / Dependencies list

配置文件 / Configuration settings

测试用例 / Test cases

<--! 黄成臻 -->

<!--by bantingrui 2205308010349-->
项目	Project
用户	User
创建	Create
更新	Update
数据模型	Data Model
初始化文件	Initialization File
令牌	Token
登录	Login
ORM 模式	ORM Mode
基础模型	Base Model
继承	Inheritance
可选字段	Optional Field
唯一标识	Unique Identifier
Pydantic 库	Pydantic Library
数据验证	Data Validation
类型提示	Type Hints
访问令牌	Access Token
令牌类型	Token Type
响应式编程	Reactive Programming
后端开发	Back-end Development
应用程序接口	Application Programming Interface (API)
数据库交互	Database Interaction
<!--by bantingrui 2205308010349-->

<!--张振锟-->
以下是middlewares文件夹代码与main.py所涉及的词汇

| 英文术语                         | 中文术语                   |
|----------------------------------|---------------------------|
| **认证与安全**                   |                          |
| OAuth2                          | OAuth2 认证协议          |
| JWT Token                       | JSON Web 令牌            |
| Bearer Token                    | 持有者令牌                |
| HTTP 401 Unauthorized           | HTTP 401 未授权状态码    |
| **Web 开发**                     |                          |
| FastAPI                         | FastAPI 框架             |
| CORS                            | 跨域资源共享             |
| Middleware                      | 中间件                   |
| RESTful API                     | RESTful 接口             |
| **Python 技术栈**                |                          |
| Pydantic Model                  | Pydantic 数据模型        |
| ORM                             | 对象关系映射             |
| Dependency Injection            | 依赖注入                 |
| ASGI                            | 异步服务器网关接口       |
| **部署与架构**                   |                          |
| Uvicorn                         | Uvicorn 服务器           |
| Production-grade Deployment     | 生产级部署               |
| **工程化结构**                   |                          |
| `__init__.py`                   | Python 包标识文件        |
| Modular Development             | 模块化开发               |
<!--张振锟-->


<!-- by 2205308010338蒙思勇 -->
英文词汇	    中文翻译
sqlalchemy	    SQLAlchemy（一个Python的SQL工具包和对象关系映射工具）
Boolean	        布尔值（布尔类型）
Column	        列（数据库表中的列）
ForeignKey	    外键
Integer	        整型
String	        字符串
relationship	关系（用于定义表之间的关系）
database	    数据库
Base	        基类（在SQLAlchemy中用于定义模型的基类）
tablename	    表名
primary_key	    主键
title	        标题（字段名）
user_id	        用户ID（字段名）
back_populates	反向填充（用于设置关系的反向引用）

schemas	        模式（在编程中通常指数据的结构定义）
users	        用户（模块名或表名）
engine	        引擎（在SQLAlchemy中指数据库引擎）
index	        索引（函数名，通常用于表示入口或初始化功能）
metadata	    元数据（数据库表的结构信息）
create_all	    创建所有（方法名，用于创建数据库表）

JSON	        JSON（JavaScript Object Notation，一种轻量级数据交换格式）
email	        邮箱（字段名）
name	        姓名（字段名）
password	    密码（字段名）
is_active	    是否激活（字段名）
nullable	    是否可为空（字段属性）
server_default	服务器默认值（字段属性）
projects	    项目（字段名，表示用户关联的项目）
user	        用户（字段名，表示项目关联的用户）
from	        从 (用于导入模块或模块中的特定对象)
import	        导入 (用于导入模块)
class	        类
def	            定义 (用于定义一个函数)
<!-- by 2205308010338蒙思勇 -->


