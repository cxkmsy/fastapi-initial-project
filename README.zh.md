            FastAPI 模型模块
  本模块定义了 FastAPI 项目中使用的核心数据模型，涵盖与项目和用户相关的数据结构。

✨ 特性
  清晰的模型定义：利用 Pydantic 库，精确地定义项目和用户的数据结构。
  支持创建和更新操作：提供用于创建和更新项目及用户的模型。
  ORM 模式兼容性：数据模型支持 ORM 模式，实现与数据库的高效交互。

📦 项目结构

fastapi - initial - project/
└── app/
    └── models/
        ├── __init__.py  # 初始化文件
        ├── projects.py  # 项目相关数据模型
        └── users.py     # 用户相关数据模型