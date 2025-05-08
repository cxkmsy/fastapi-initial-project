# FastAPI Starter Project

## Introduction

This is a starter project template based on the [FastAPI](https://fastapi.tiangolo.com/) framework, designed to help developers quickly bootstrap Python-based web applications. The project adopts a modular architecture, supporting rapid development, extension, and deployment.

---

## Key Features

- 🚀 **Quick Startup**: Minimal FastAPI project structure included
- 🛠️ **Extensible**: Modular code structure for easy feature expansion
- 📦 **Dependency Management**: Managed via `requirements.txt` or `poetry`
- 🔐 **Security**: Built-in environment variables support (`.env` file)
- 🗃️ **Database Support**: Compatible with multiple databases (SQLite, PostgreSQL, etc.)
- 🌐 **API Documentation**: Auto-generated interactive API docs (Swagger UI & ReDoc)

---

## Environment Requirements

Before proceeding, ensure your development environment meets the following requirements:

- Python version: `>=3.8`
- Recommended OS: Windows, MacOS, Linux
- Package manager: `pip` or `poetry`

---

## Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/zzk-zuishuai/fastapi-initial-project.git
cd fastapi-initial-project
```

### 2. Create Virtual Environment

Create and activate virtual environment using `venv`:

```bash
python -m venv venv
# Activate (Linux/MacOS)
source venv/bin/activate
# Activate (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage Guide

### Run Development Server

Start server in development mode:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

After server starts, access these endpoints:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Database Migrations

If using databases, run migration scripts:

```bash
alembic upgrade head
```

---

## Deployment Guide

### 1. Gunicorn Deployment

```bash
gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
```

### 2. Nginx Reverse Proxy

Sample Nginx configuration:

```nginx
server {
    listen 80;
    server_name your_domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 3. Docker Deployment (Optional)

Create `Dockerfile`:

```dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run Docker image:

```bash
docker build -t fastapi-app .
docker run -d -p 8000:8000 fastapi-app
```

---

## Directory Structure

```plaintext
fastapi-initial-project/
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── routers/         # API route modules
│   ├── models/          # Database models
│   ├── schemas/         # Data validation schemas
│   └── utils/           # Utility functions
├── tests/               # Test cases
├── requirements.txt     # Dependency list
├── Dockerfile           # Docker configuration
└── README.md            # Project documentation
```
<!--zhangzhenkun-->