
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

<!-- by wenliangfeng -->
# AI 修改记录文档
# 修改文件
1. `README.md` 
2. `README.zh.md`
3. `terms.md`
4. `ai_usage_screenshots`

# AI 辅助内容
DeepSeek Chat：
为一些技术术语提供中英文对照表：截图：ai_usage_screenshots/2205308010327_1.png
解决二次提交代码远近仓库中因未更新无法提交代码的问题：截图：ai_usage_screenshots/2205308010327_2.png
用git命令查看提交记录：截图：ai_usage_screenshots/2205308010327_3.png
审核中英文术语一致性
生成安全配置参数对照表

# 修改文件
1. `auth.py`
2. `hashing.py`

<!-- by wenliangfeng -->


## 2205308010313 李念毅
  - 使用AI解释代码，了解代码的意思
  - 优化术语表格式（DeepSeek Chat）

  - AI辅助编写API内容
  - 自动生成API示例代码（GitHub Copilot）

  - AI辅助理解并改进代码
  - 检查内容是否有误，并优化内容
## 2205308010313 李念毅

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

<!--by bantingrui 2205308010349-->
以下是针对 projects.py 和 users.py 中模型可能出现的问题及相应解决方案：
1. 模型定义问题
问题描述
字段类型不匹配：在数据库操作时，模型字段类型与数据库字段类型不一致，导致数据存储或查询出错。
必填字段缺失：创建或更新对象时，遗漏了模型中定义的必填字段。
解决方案
检查字段类型：确保 pydantic 模型中的字段类型与数据库表结构一致。例如，如果数据库中的 id 字段是整数类型，那么模型中对应的 id 字段也应该定义为 int 类型。
处理必填字段：在创建或更新对象时，验证必填字段是否提供。可以在业务逻辑中添加验证逻辑，确保所有必填字段都有值。
2. 模型关联问题
问题描述
关联关系定义错误：在 projects.py 中，Project 模型与 User 模型存在关联关系（通过 user_id），如果关联关系定义错误，会导致数据关联不准确。
关联查询失败：在查询 Project 时，无法正确关联到对应的 User 信息。
解决方案
正确定义关联关系：在数据库层面，确保 Project 表中的 user_id 字段与 User 表中的 id 字段建立了正确的外键关系。在模型层面，使用相应的 ORM 工具（如 SQLAlchemy）来定义关联关系。
优化关联查询：使用 ORM 工具提供的关联查询功能，确保在查询 Project 时能够正确关联到对应的 User 信息。例如，使用 SQLAlchemy 的 join 方法进行关联查询。
3. 数据验证问题
问题描述
数据格式不符合要求：用户输入的数据格式不符合模型定义的要求，例如 email 字段不是有效的电子邮件地址。
数据范围超出限制：某些字段有取值范围限制，如 is_active 字段只能是 True 或 False，如果输入的值超出了这个范围，会导致数据验证失败。
解决方案
添加数据验证逻辑：在 pydantic 模型中使用验证器（@validator）来添加自定义的数据验证逻辑。例如，使用正则表达式验证 email 字段是否为有效的电子邮件地址。
处理数据范围限制：在模型定义中明确字段的取值范围，并在数据验证时进行检查。如果输入的值超出了范围，可以返回相应的错误信息。
4. 模型序列化与反序列化问题
问题描述
序列化失败：将模型对象转换为 JSON 或其他格式时，出现错误。
反序列化失败：将 JSON 或其他格式的数据转换为模型对象时，出现错误。
解决方案
检查序列化配置：确保 pydantic 模型的 Config 类中 orm_mode 配置正确，以便在序列化和反序列化时能够正确处理 ORM 对象。
处理序列化和反序列化错误：在业务逻辑中捕获并处理序列化和反序列化过程中可能出现的错误，返回清晰的错误信息。
问题排查流程图
问题发生 → 检查日志 / 错误信息
→ 定位问题模块（模型定义 / 关联关系 / 数据验证 / 序列化反序列化）
→ 验证依赖项版本（Pydantic/ORM 工具）
→ 单元测试复现问题
→ 修复并验证
<!--by bantingrui 2205308010349-->


<!--张振锟-->
以下是三个文件（auth.py、main.py 和 `__init__.py`）在开发中所遇到的问题及通过询问AI获得的解决方案：


### **1. 认证问题 (auth.py)**
| 问题描述                     | 解决方案                                                                 |
|------------------------------|--------------------------------------------------------------------------|
| **令牌验证失败**：JWT 过期、签名错误或用户不存在 | 检查令牌生成/验证逻辑，确保密钥一致，添加异常捕获和清晰的错误提示          |
| **依赖注入失效**：`get_current_user` 无法正确获取用户 | 确认路由中正确使用 `Depends()`，检查用户数据库查询逻辑                    |
| **OAuth2 流程错误**：无法通过 `/user/login` 获取 token | 验证密码哈希逻辑，检查请求格式是否符合 `OAuth2PasswordRequestForm` 规范   |

---

### **2. 路由与配置问题 (main.py)**
| 问题描述                     | 解决方案                                                                 |
|------------------------------|--------------------------------------------------------------------------|
| **CORS 跨域错误**：前端请求被浏览器拦截 | 检查 `CORSMiddleware` 配置，确保 `allow_origins` 包含正确的前端域名或 `*` |
| **路由未加载**：新增的 API 端点无法访问 | 确认路由已通过 `indexRoute.load_routes(app)` 正确注册                     |
| **生产部署失败**：Uvicorn 服务无法启动 | 检查端口占用情况，使用 `--workers` 配置多进程，添加 `--proxy-headers` 选项 |

---

### **3. 包结构问题 (`__init__.py`)**
| 问题描述                     | 解决方案                                                                 |
|------------------------------|--------------------------------------------------------------------------|
| **模块导入错误**：`from app.auth import ...` 失败 | 确保所有包目录包含 `__init__.py`（Python 3.3+ 可省略但建议保留）          |
| **循环依赖**：模块间相互引用导致启动崩溃 | 重构代码结构，将公共依赖提取到独立模块，使用延迟导入（Lazy Import）       |

---

### **4. 其他常见问题**
| 问题描述                     | 解决方案                                                                 |
|------------------------------|--------------------------------------------------------------------------|
| **性能问题**：API 响应缓慢   | 启用 GZip 压缩中间件，优化数据库查询，使用缓存机制（如 Redis）           |
| **配置泄露**：敏感信息（如密钥）硬编码在代码中 | 将配置移至环境变量或 `.env` 文件，使用 `python-dotenv` 加载              |
| **文档缺失**：API 接口无文档 | 为路由添加 Swagger 注释，利用 FastAPI 自动生成 `/docs` 接口文档           |

---

### **问题排查流程图**
```
问题发生 → 检查日志/错误信息 
    → 定位问题模块（认证/路由/配置） 
    → 验证依赖项版本（FastAPI/Pydantic/Uvicorn） 
    → 单元测试复现问题 
    → 修复并验证
```
<!--张振锟-->


<!-- by 2205308010338蒙思勇 -->
1、错误信息：重复定义了数据库表，或者模型类未正确继承 Base。
ai给出解决方法：确保所有模型类都继承自 Base（通常从 app.database 中导入），检查是否有重复的表名。

2、错误信息：数据库未创建或未正确连接。
ai给出解决方法：确保数据库已创建。检查 config.py 中的数据库配置是否正确。

3、错误信息：数据库字段类型与模型定义不匹配。
ai给出解决方法：检查模型字段类型是否与数据库表字段类型一致。如果修改了模型字段类型，确保同步更新数据库表结构。

4、错误信息：环境变量缺失。
ai给出解决方法：检查 .env 文件或环境变量配置是否正确。

5、错误信息：未正确安装依赖。
ai给出解决方法：pip install fastapi

<!-- by 2205308010338蒙思勇 -->

