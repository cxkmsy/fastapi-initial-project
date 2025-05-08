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

<!-- by wenliangfeng -->