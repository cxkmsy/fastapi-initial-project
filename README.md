# FastApi_best_practice_pattern

### Best Object-Oriented pattern for FastApi framework with Authentication and error handling  

- Create a Virtual Environment and run `pip install -r requirements.txt` to install the dependencies.
- Create an empty database (default name in the project is `test_db`).
- Change the app/config.py based on your MySql credential.
- Run `uvicorn main:app --reload` in command line.
- Open `http://127.0.0.1:8000/docs` in the browser.


# FastAPI Routes Module

This module contains the main API route definitions for user management and project management features.

## 🚀 Features

- 👥 Complete user authentication system (login/register)
- 🔐 JWT-based authorization
- 📦 Project CRUD operations
- 🛡️ Route-level permission validation

## 📂 File Structure
router/
├── init.py # Package initialization
├── index.py # Route loading entry
├── projects.py # Project-related routes
└── users.py # User-related routes

#2205308010313 李念毅
## 🛠️ Route Specifications

![Screenshot of project interface](images/users3.png)
### User Routes (/user)
- `GET /user` - Get all users (Authentication required)
- `POST /user` - Create new user
- `GET /user/{id}` - Get specific user details (Auth required)
- `PUT /user/{id}` - Update user information (Auth required)
- `DELETE /user/{id}` - Delete user (Auth required)
- `POST /user/login` - User login (Get access token)

![Screenshot of project interface](images/proje)
### Project Routes (/project)
- `GET /project` - Get all projects (Auth required)
- `POST /project` - Create new project (Auth required)
- `GET /project/{id}` - Get specific project details (Auth required)
- `PUT /project/{id}` - Update project information (Auth required)
- `DELETE /project/{id}` - Delete project (Auth required)

## 🏗️ Development Guide

1. Register new route files in `index.py`
2. Use `dependencies` parameter of `APIRouter` to add route-level middleware
3. Consistently use response models defined in `app.models`