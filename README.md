
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

<!-- by 2205308010338蒙思勇 -->
# FATSAPI Project

This is a task management tool based on "FastAPI" and "Vue.js", designed to help users manage tasks efficiently. The project is suitable for learning and practicing full-stack development, especially the combination of FastAPI and Vue.js.

✨ Project Features
📝 Task Management: Supports adding, editing, and deleting tasks to help users plan and manage their daily tasks clearly.
✅ Task Status Management: Allows users to check off tasks as completed, making it easy to track progress.
💾 Data Storage:
Frontend: Supports browser LocalStorage for task data storage, facilitating a quick experience.
Backend: Uses a database (such as MySQL) to store task data, ensuring data persistence.
🎨 Responsive Design: The interface is adapted for both mobile phones and PCs, providing a good user experience.
🔗 API Support: The backend provides RESTful APIs, making it easy to integrate with other systems.
🚀 Quick Start
Clone the Project
bash
复制
git clone https://github.com/cxkmsy/fastapi-initial-project.git  
cd fastapi-initial-project
Backend Part
Install Dependencies:
bash
复制
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
Configure Database:
Ensure MySQL or another database is installed and running.
Modify the database configuration in the app/config.py file.
Initialize Database:
bash
复制
python -c "from app.schemas.schema import index; index()"
Run Backend Service:
bash
复制
uvicorn app.main:app --reload
The backend service will run at http://127.0.0.1:8000.
Frontend Part
Install Dependencies:
bash
复制
cd frontend
npm install
Start Frontend Service:
bash
复制
npm run dev
The frontend service will run at http://localhost:5173.
📮 API Documentation
The backend provides automatically generated API documentation accessible at the following addresses:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
📦 Project Structure
复制
fastapi-initial-project/
├── app/                  # Backend code directory
│   ├── controllers/      # Controller modules for handling business logic
│   │   ├── __init__.py   # Package initialization file
│   │   ├── projects.py   # Business logic related to projects
│   │   ├── users.py      # Business logic related to users
│   ├── helpers/          # Helper tool modules
│   │   ├── __init__.py   # Package initialization file
│   │   ├── auth.py       # Authentication-related utility functions
│   │   ├── hashing.py    # Hash processing tools (e.g., password encryption)
│   ├── middlewares/      # Middleware modules
│   │   ├── __init__.py   # Package initialization file
│   │   ├── auth.py       # Authentication middleware
│   ├── models/           # Database model definitions
│   │   ├── __init__.py   # Package initialization file
│   │   ├── projects.py   # Project models
│   │   ├── users.py      # User models
│   ├── routers/          # Routing modules
│   │   ├── __init__.py   # Package initialization file
│   │   ├── index.py      # Routing entry point
│   │   ├── projects.py   # Routing related to projects
│   │   ├── users.py      # Routing related to users
│   ├── schemas/          # Data validation and serialization modules
│   │   ├── __init__.py   # Package initialization file
│   │   ├── projects.py   # Pydantic models related to projects
│   │   ├── schema.py     # Database initialization script
│   │   ├── users.py      # Pydantic models related to users
│   ├── __init__.py       # Package initialization file
│   ├── config.py         # Configuration file (e.g., database connection settings)
│   ├── database.py       # Database connection and initialization
│
├── .gitignore            # Git ignore file configuration
├── LICENSE               # Project license
├── main.py               # Main entry point of the FastAPI application
├── README.md             # English version of the project documentation
├── README.zh.md          # Chinese version of the project documentation
├── requirements.txt      # List of Python dependencies
├── terms.md              # Project terms or description
├── ai_usage_screenshots  # Directory for AI usage screenshots
📸 Project Features and Screenshots
1. Add Task
Users can add new tasks by entering the task name and description.
![Add Task Interface]
2. View Task List
The task list displays all tasks, including incomplete and completed tasks.
![Task List Interface]
3. Edit Task
Supports modifying existing tasks, including task name and description.
![Edit Task Interface]
4. Delete Task
Users can delete tasks that are no longer needed.
![Delete Task Interface]
5. Check Off Completed Tasks
By checking off tasks, mark tasks as completed.
![Check Off Task Interface]
<!-- by 2205308010338蒙思勇 -->

