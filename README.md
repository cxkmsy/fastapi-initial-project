# FastAPI Initial Project - Controller Module Introduction

This project is a FastAPI-based initial project. The controller module (controllers) is primarily responsible for handling business logic, including operations related to projects and users.

## ✨ Project Features

- Provides CRUD operations for projects and users.
- Implements exception handling for database operations to enhance system stability.
- Supports user login and JWT token authentication.

## 🚀 Quick Start

### Clone the Project

git clone [Your Project Repository URL]
cd [Project Folder Name]

### Install Dependencies

pip install -r requirements.txt

### Start the Project

uvicorn main:app --reload

The project will run at http://localhost:8000
<!--------------------------------------------- by2205308010333徐济艺 ------------------------------------------------------------->

## 📦 Project Structure
fastapi-initial-project-master/
├── app/
│   ├── controllers/
│   │   ├── projects.py  # Project-related controllers
│   │   └── users.py     # User-related controllers
│   ├── helpers/
│   ├── middlewares/
│   ├── models/
│   ├── routers/
│   └── schemas/
└── ...

## 📮 Main Project Functions and Screenshots
1. User Management Functions (Corresponding to users.py)

- User Registration (create function)
  Functionality: Receives user registration requests, encrypts passwords, and stores them in the database.

![Screenshot of user registration code](images/1.png)


- User Login (login function)
  Functionality: Verifies user email and password, generates and returns a JWT authentication token.

![Screenshot of user login code](images/2.png)

- Query a Single User (get_one function)
  Functionality: Retrieves user details by user ID, returns a 404 error if not found.

![Query the screenshot of a single user's code](images/3.png)

- Update User Information (update function)
  Functionality: Supports updating user information (including password, which is automatically encrypted), returns a 404 error if the user is not found.
  ![Screenshots of the code for updating user information](images/4.png)

- Delete User (destroy function)
  Functionality: Deletes a user by user ID, returns a 404 error if not found.
  ![Delete screenshots of user code](images/5.png)

1. Project Management Functions (Corresponding to projects.py)

- Create Project (create function)
  Functionality: Creates a new project, force association of user_id (ensures each project belongs to a specific user).
  ![Create screenshots of project code](images/6.png)

- Query All Projects (get_all function)
  Functionality: Returns all project records in the database (in practice, filtering by user ID may be required; current code does not reflect this, but documentation should state "filter projects by the current user using authentication logic").
  ![Query screenshots of all project codes](images/7.png)

- Query a Single Project (get_one function)
  Functionality: Retrieves project details by project ID, returns a 404 error if not found.
  ![Query the screenshot of a single project code](images/8.png)

- Update Project (update function)
  Functionality: Updates project information by project ID, returns a 404 error if not found.
  ![Update screenshots of the project code](images/9.png)

- Delete Project (destroy function)
  Functionality: Deletes a project by project ID, returns a 404 error if not found.
  ![Delete screenshots of project code](images/10.png)

1. Authentication Mechanism (Corresponding to users.py)

- JWT Token Generation (create_access_token function)
  Functionality: Generates a JWT token with an expiration time for user authentication.
  ![Screenshot of JWT token generation code](images/11.png)

- JWT Token Verification (verify_token function)
  Functionality: Verifies the validity of a JWT token and extracts the user email for permission verification.
  ![Screenshot of JWT token verification code](images/12.png)
  <!--------------------------------------------- by2205308010333徐济艺 ------------------------------------------------------------->

