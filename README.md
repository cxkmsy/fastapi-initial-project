# FastApi_best_practice_pattern

### Best Object-Oriented pattern for FastApi framework with Authentication and error handling  

- Create a Virtual Environment and run `pip install -r requirements.txt` to install the dependencies.
- Create an empty database (default name in the project is `test_db`).
- Change the app/config.py based on your MySql credential.
- Run `uvicorn main:app --reload` in command line.
- Open `http://127.0.0.1:8000/docs` in the browser.


                    FastAPI Model Module(by 班庭锐)
  This module defines the core data models used in the FastAPI project, covering data structures related to projects and users.

✨ Features

  Clear Model Definitions: Utilize the Pydantic library to precisely define the data structures for projects and users.

  Support for Creation and Update Operations: Provide models for creating and updating projects and users.

   ORM Mode Compatibility: The data models support ORM mode, enabling efficient interaction with the database.

📦 Project Structure

fastapi-initial-project/
└── app/
    └── models/
        ├── __init__.py  # Initialization file
        ├── projects.py  # Project-related data models
        └── users.py     # User-related data models