<--! huang cheng zhen -->
### README.md

### 🇺🇸 English Version

## ✨ Features

- 🏗️ Object-Oriented design pattern
- 🔐 JWT Authentication system
- 🛡️ Comprehensive error handling
- 🗃️ MySQL database support
- 📝 Automatic API documentation (Swagger UI)

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/cxkmsy/fastapi-initial-project.git
cd fastapi-initial-project-master
```

### 2. Create virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3. Database configuration
Modify database connection in `app/config.py`:
```python
DB_HOST: str = "localhost"     # Database host
DB_PORT: str = "3306"          # Database port
DB_NAME: str = "test_db"       # Database name
DB_USER: str = "root"          # Database user
DB_PASS: str = "rootroot"      # Database password
```

### 4. Run the application
```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for API documentation

## ⚙️ Core Configuration

### Authentication
```python
SECRET_KEY = "09d25e094faa..."  # JWT secret key
ALGORITHM = "HS256"            # Encryption algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Token expiration time
```

### Database Connection
Using SQLAlchemy ORM, configured in `app/database.py`:
```python
# MySQL connection string format
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:password@host:port/dbname?charset=utf8mb4"

# Database session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

## 📦 Project Structure
```
fastapi-project/
├── app/
│   ├── controllers/          # Business logic handlers
│   │   ├── __init__.py
│   │   ├── projects.py
│   │   └── users.py
│   ├── helpers/             # Utility helpers
│   │   ├── __init__.py
│   │   ├── auth.py          # Authentication helpers
│   │   └── hashing.py       # Hashing utilities
│   ├── middlewares/         # Middleware components
│   │   ├── __init__.py
│   │   └── auth.py          # Authentication middleware
│   ├── models/              # Database models
│   │   ├── __init__.py
│   │   ├── projects.py
│   │   └── users.py
│   ├── routers/             # API routers
│   │   ├── __init__.py
│   │   ├── index.py         # Root router
│   │   ├── projects.py
│   │   └── users.py
│   ├── schemas/             # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── projects.py
│   │   ├── schema.py        # Base schemas
│   │   └── users.py
│   ├── __init__.py          # Application initialization
│   ├── config.py            # Configuration settings
│   └── database.py          # Database connection
├── tests/                   # Test cases
├── venv/                    # Virtual environment
├── .gitignore
├── LICENSE
├── main.py                  # Application entry point
├── README.md
└── requirements.txt         # Dependencies list
<--! by huang cheng zhen -->
```