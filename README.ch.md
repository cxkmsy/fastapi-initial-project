<--! 黄成臻 -->
### README.ch.md

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
---