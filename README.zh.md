<!-- by 2205308010338蒙思勇 -->
# FATSAPI 项目

这是一个基于 "FastAPI" 和 "Vue.js" 的任务管理工具，旨在帮助用户高效地管理任务。项目适合用来学习和实践全栈开发，尤其是 FastAPI 和 Vue.js 的结合使用。

## ✨ 项目特点

- 📝 "任务管理"：支持添加、编辑、删除任务，帮助用户清晰地规划和管理日常任务。
- ✅ "任务状态管理"：可以勾选任务为已完成状态，方便用户跟踪任务进度。
- 💾 "数据存储"：
  - 前端：支持浏览器 LocalStorage 存储任务数据，便于快速体验。
  - 后端：使用数据库（如 MySQL）存储任务数据，确保数据持久化。
- 🎨 "响应式设计" ：界面适配手机和 PC，提供良好的用户体验。
- 🔗 "API 支持"  ：后端提供 RESTful API，方便与其他系统集成。

## 🚀 快速开始

### 克隆项目

```bash
https://github.com/cxkmsy/fastapi-initial-project.git
cd fastapi-initial-project
```

### 后端部分

1. **安装依赖**：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

2. **配置数据库**：
   - 确保 MySQL 或其他数据库已安装并运行。
   - 修改 `app/config.py` 文件中的数据库配置。

3. **初始化数据库**：
   ```bash
   python -c "from app.schemas.schema import index; index()"
   ```

4. **运行后端服务**：
   ```bash
   uvicorn app.main:app --reload
   ```
   后端服务将运行在 `http://127.0.0.1:8000`。

### 前端部分

1. **安装依赖**：
   ```bash
   cd frontend
   npm install
   ```

2. **启动前端服务**：
   ```bash
   npm run dev
   ```
   前端服务将运行在 `http://localhost:5173`。

## 📮 API 文档

后端提供了自动生成的 API 文档，可以通过以下地址访问：
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`


## 📦 项目结构

```
fastapi-initial-project/
├── app/                  # 后端代码目录
│   ├── controllers/      # 控制器模块，处理业务逻辑
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── projects.py   # 项目相关的业务逻辑
│   │   ├── users.py      # 用户相关的业务逻辑
│   ├── helpers/          # 辅助工具模块
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── auth.py       # 认证相关的工具函数
│   │   ├── hashing.py    # 哈希处理工具（如密码加密）
│   ├── middlewares/      # 中间件模块
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── auth.py       # 认证中间件
│   ├── models/           # 数据库模型定义
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── projects.py   # 项目模型
│   │   ├── users.py      # 用户模型
│   ├── routers/          # 路由模块
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── index.py      # 路由加载入口
│   │   ├── projects.py   # 项目相关的路由
│   │   ├── users.py      # 用户相关的路由
│   ├── schemas/          # 数据验证和序列化模块
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── projects.py   # 项目相关的 Pydantic 模型
│   │   ├── schema.py     # 数据库初始化脚本
│   │   ├── users.py      # 用户相关的 Pydantic 模型
│   ├── __init__.py       # 包初始化文件
│   ├── config.py         # 配置文件（如数据库连接配置）
│   ├── database.py       # 数据库连接和初始化
│
├── .gitignore            # Git 忽略文件配置
├── LICENSE               # 项目许可证
├── main.py               # FastAPI 应用主入口
├── README.md             # 英文版项目说明文档
├── README.zh.md          # 中文版项目说明文档
├── requirements.txt      # Python 依赖列表
├── terms.md              # 项目条款或说明
├── ai_usage_screenshots  # AI 使用截图目录
```

## 📸 项目功能与截图

### 1. 添加任务
用户可以通过输入任务名称和描述来添加新任务。

![添加任务界面]

### 2. 查看任务列表
任务列表展示所有任务，包括未完成和已完成的任务。

![任务列表界面]

### 3. 编辑任务
支持对已有任务进行修改，包括任务名称和描述。

![编辑任务界面]

### 4. 删除任务
用户可以删除不需要的任务。

![删除任务界面]

### 5. 勾选已完成任务
通过勾选任务，标记任务为已完成状态。

![勾选任务界面]
<!-- by 2205308010338蒙思勇 -->