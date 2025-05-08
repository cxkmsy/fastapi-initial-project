<!-- by wenliangfeng -->

# Authentication Module

# Clone the Project
git clone https://github.com/wenliangfeng/fastapi-initial-project.git
cd fastapi-initial-project

The authentication system module under `app/helpers/` provides secure user authentication features including:
JWT token generation and verification (`auth.py`)
Password hashing and verification (`hashing.py`)

# ✅ Key Features
Stateless authentication using JWT
Secure password hashing with Bcrypt
Configurable token expiration time
Auto-salted password encryption

# Installation
pip install python-jose[cryptography] passlib bcrypt

# Environment Configuration
Add to `.env` file:
SECRET_KEY=your_random_secret_key_here
ALGORITHM=HS256
DEFAULT_EXPIRATION_TOKEN=30  # in minutes

# Core Functionality
python
from app.helpers.auth import create_access_token, decode_token
from app.helpers.hashing import get_password_hash, verify_password
from datetime import timedelta

# Generate token
token = create_access_token(
    data={"user_id": 123},
    expires_delta=timedelta(hours=2)
)

# Password hashing and verification
hashed_pw = get_password_hash("mypassword")
verify_password("mypassword", hashed_pw)  # Returns True/False

🏗️ Project Structure
app/
└── helpers/
    ├── auth.py           # JWT authentication core
    ├── hashing.py        # Password hashing
    └── __init__.py       # Module exports

📸 Feature Screenshots
1. Access Token Generation
Token Generation Flow
Figure 1: JWT access token creation process

2. Password Verification Flow
Password Verification
Figure 2: Password hashing and verification workflow

📚 Technology Stack
| Technology | Purpose | Version Requirement |
|------------|---------|---------------------|
| python-jose | JWT implementation | >=3.3.0 |
| passlib | Password hashing | >=1.7.4 |
| bcrypt | Hashing algorithm | >=4.0.1 |

<!-- by wenliangfeng -->
