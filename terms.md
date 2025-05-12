
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

<!-- by wenliangfeng -->
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

