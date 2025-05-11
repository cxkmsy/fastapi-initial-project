<--! 黄成臻 -->
配置与数据库设置
1. 配置类 (Settings)
基础配置

使用 Pydantic 的 BaseSettings 管理配置，支持从环境变量读取。

默认数据库配置：

DB_HOST: str = "localhost"  # 数据库主机
DB_PORT: str = "3306"       # 数据库端口
DB_NAME: str = "test_db"    # 数据库名
DB_USER: str = "root"       # 数据库用户
DB_PASS: str = "rootroot"   # 数据库密码
JWT 认证配置

添加了安全相关参数：

SECRET_KEY = "09d25e..."    # 密钥（需替换为实际环境变量）
ALGORITHM = "HS256"         # 加密算法
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token 过期时间
文件类型常量

用常量标识文件类型（如 BACKGROUND = 1），避免魔法数字。

2. 数据库连接
SQLAlchemy 初始化

动态生成数据库连接 URL：

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}?charset=utf8mb4"
创建引擎和会话工厂：

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
依赖注入

通过 get_db() 管理会话生命周期，确保资源释放：

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
<--! 黄成臻 -->