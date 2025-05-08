# FastAPI 初始项目

## 简介

这是一个基于 [FastAPI](https://fastapi.tiangolo.com/) 框架的初始项目模板，旨在帮助开发者快速启动基于 Python 的 Web 应用程序。该项目采用模块化设计，支持快速开发、扩展和部署。

---

## 功能特性

- 🚀 **快速启动**：包含最小化的 FastAPI 项目结构。
- 🛠️ **可扩展**：模块化代码结构，易于扩展新功能。
- 📦 **依赖管理**：使用 `requirements.txt` 或 `poetry` 管理依赖。
- 🔐 **安全性**：内置支持环境变量管理（`.env` 文件）。
- 🗃️ **数据库支持**：支持多种数据库（如 SQLite、PostgreSQL）。
- 🌐 **API 文档**：自动生成交互式 API 文档（Swagger UI 和 ReDoc）。

---

## 环境要求

在开始之前，请确保您的开发环境满足以下要求：

- Python 版本：`>=3.8`
- 推荐操作系统：Windows、MacOS、Linux
- 包管理工具：`pip` 或 `poetry`

---

## 安装步骤

### 1. 克隆项目代码

```bash
git clone https://github.com/zzk-zuishuai/fastapi-initial-project.git
cd fastapi-initial-project
```

### 2. 创建虚拟环境

使用 `venv` 创建虚拟环境并激活：

```bash
python -m venv venv
# 激活虚拟环境 (Linux/MacOS)
source venv/bin/activate
# 激活虚拟环境 (Windows)
venv\Scripts\activate
```

### 3. 安装项目依赖

```bash
pip install -r requirements.txt
```

---

## 使用说明

### 运行开发服务器

在开发模式下运行服务器：

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

服务器启动后，您可以访问以下地址：

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 数据库迁移

如果项目使用了数据库，请确保运行迁移脚本：

```bash
alembic upgrade head
```

---

## 部署指南

以下是生产环境的部署步骤示例：

### 1. 使用 Gunicorn 部署

```bash
gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
```

### 2. 配置 Nginx 反向代理

以下是 Nginx 配置示例：

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

### 3. 使用 Docker 部署（可选）

创建一个 `Dockerfile`：

```dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

构建并运行 Docker 镜像：

```bash
docker build -t fastapi-app .
docker run -d -p 8000:8000 fastapi-app
```

---

## 目录结构

以下是项目的主要目录结构：

```plaintext
fastapi-initial-project/
├── app/
│   ├── main.py          # FastAPI 应用入口
│   ├── routers/         # 路由模块
│   ├── models/          # 数据模型
│   ├── schemas/         # 数据验证模型
│   └── utils/           # 工具函数
├── tests/               # 测试代码
├── requirements.txt     # 项目依赖
├── Dockerfile           # Docker 配置
└── README.md            # 项目说明文档
```
<!--张振锟-->
---
