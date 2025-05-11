<!--by bantingrui 2205308010349-->
                    FastAPI Model Module(models file）(by bantingrui 2205308010349)

  This module defines the core data models used in the FastAPI project, covering data structures related to projects and users.

✨ Features

Clear Model Definitions: Utilize the Pydantic library to precisely define the data structures for projects and users.

Support for Creation and Update Operations: Provide models for creating and updating projects and users.

ORM Mode Compatibility: The data models support ORM mode, enabling efficient interaction with the database.

📦 Project Structure

fastapi-initial-project/
└── app/
└── models/
├── **init**.py # Initialization file
├── projects.py # Project-related data models
└── users.py # User-related data models

📮 Core Model Analysis (by Bantingrui)​
I. Project Models (projects.py)​

1. Basic Project Information Model (ProjectBase)​
   Define the basic fields of a project, serving as the base class for other models:​
   ​
   from pydantic import BaseModel​
   class ProjectBase(BaseModel):​
   title: str​
   ​
2. Project Creation Model (ProjectCreate)​
   Inherit from ProjectBase and add the user_id field (required) to specify the ID of the user who created the project:​
   ​
   class ProjectCreate(ProjectBase):​
   user_id: int​
   ​
3. Project Update Model (ProjectUpdate)​
   Inherit from ProjectBase, with fields set as optional to support partial updates:​
   ​
   from typing import Optional​
   class ProjectUpdate(ProjectBase):​
   title: Optional[str] = None​
   ​
4. Complete Project Information Model (Project)​
   Inherit from ProjectBase, add database fields (ID, user_id), and enable ORM mode:​
   ​
   class Project(ProjectBase):​
   id: int​
   user_id: int​
   class Config:​
   orm_mode = True # Support conversion from SQLAlchemy models​
   ​
   II. User Models (users.py)​
   **1. Basic User Information Model (UserBase)​**
   Define the basic fields of a user (name, email, active status):​
   ​
   class UserBase(BaseModel):​
   name: str​
   email: str​
   is_active: bool​
   ​
   **2. User Creation Model (UserCreate)​**
   Inherit from UserBase and add the password field (required for user registration):​
   ​
   class UserCreate(UserBase):​
   password: str​
   ​
   **3. User Update Model (UserUpdate)​**
   Inherit from UserBase, with all fields set as optional to support partial updates:​
   ​
   class UserUpdate(UserBase):​
   name: Optional[str] = None​
   email: Optional[str] = None​
   password: Optional[str] = None​
   is_active: Optional[bool] = None​
   ​
   **4. Complete User Information Model (User)​**
   Inherit from UserBase, add the user ID, and enable ORM mode:​
   ​
   class User(UserBase):​
   id: int​
   class Config:​
   orm_mode = True​
   \*\*​
5. User Login Model (UserLogin)​**
   Used for user authentication, containing email and password fields (verified during login):​
   ​
   class UserLogin(BaseModel):​
   email: str​
   password: str​
   class Config:​
   orm_mode = True​
   ​
   **6. Token Model (Token)​**
   Represents the token structure returned after a user logs in (access token, token type):​
   ​
   class Token(BaseModel):​
   access_token: str​
   token_type: str​
   class Config:​
   orm_mode = True​
   ​
   **7. Token Data Model (TokenData)​\*\*
   Used to store data within the token, currently only including the user's email (optional):​
   ​
   from typing import Optional​
   class TokenData(BaseModel):​
   email: Optional[str] = None​
<!--by bantingrui 2205308010349-->
