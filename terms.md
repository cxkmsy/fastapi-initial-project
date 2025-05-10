1. FastAPI
- 定义：一个基于 Python 的现代高性能 Web 框架，用于快速构建 API，支持异步编程、自动生成交互式文档（Swagger/OpenAPI）和严格的类型提示。
项目应用：本项目基于 FastAPI 搭建，控制器模块（controllers）通过 FastAPI 的依赖注入和路由系统，实现对用户和项目资源的 RESTful 接口管理。
2. SQLAlchemy
- 定义：Python 中流行的 SQL 工具包和对象关系映射器（ORM），允许通过 Python 类操作数据库，将数据库表映射为对象，简化数据库交互逻辑。
项目应用：在 projects.py 和 users.py 中，通过 SQLAlchemy 的会话（Session）对象执行数据库查询（如 db.query(Project).all()），实现对项目和用户数据的增删改查操作，并处理数据库异常（如 SQLAlchemyError）。
3. JWT（JSON Web Token）
- 定义：一种开放标准（RFC 7519），用于在网络应用间安全传输信息的令牌，通常用于用户认证和授权，包含用户信息和过期时间等数据，通过签名确保不可篡改。
项目应用：在 users.py 的登录逻辑中，生成 JWT 令牌（create_access_token）并返回给客户端，后续请求通过令牌验证用户身份（verify_token），实现无状态认证。
4. 控制器（Controller）
- 定义：在 MVC（模型 - 视图 - 控制器）架构中，控制器是处理用户请求、协调模型和视图的中间层，负责接收输入、调用业务逻辑并返回响应。
项目应用：controllers 目录下的 projects.py 和 users.py 分别封装了项目和用户相关的业务逻辑，如数据验证、数据库操作和异常处理，是连接路由（routers）和模型（models）的核心模块。
5. ORM（对象关系映射）
- 定义：一种编程技术，将数据库中的表映射为编程语言中的对象，通过操作对象实现对数据库的增删改查，避免直接编写 SQL 语句，提高开发效率和代码可维护性。
项目应用：本项目通过 SQLAlchemy 的 ORM 模型（如 Project 和 User 类）定义数据库表结构，控制器中的方法（如 get_all、create）通过操作这些对象完成数据库交互，例如 db.add(new_item) 对应插入数据库记录。
6. 依赖注入（Dependency Injection）
- 定义：一种设计模式，通过将依赖（如数据库会话、配置对象）传递给函数或类，而非硬编码，提高代码的松耦合性和可测试性。
项目应用：FastAPI 原生支持依赖注入，控制器函数（如 get_all(db: Session)）通过参数声明依赖（如 db: Session），框架会自动解析并注入数据库会话，简化资源管理。

1. FastAPI
- Definition: A modern, high-performance Python-based Web framework for rapidly building APIs. It supports asynchronous programming, automatic generation of interactive documentation (Swagger/OpenAPI), and strict type hints.
Project application: This project is built on FastAPI. The controller module (controllers) uses FastAPI's dependency injection and routing system to implement RESTful interface management for user and project resources.
2. SQLAlchemy
- Definition: A popular SQL toolkit and object-relational mapper (ORM) in Python. It allows database operations through Python classes by mapping database tables to objects, simplifying database interaction logic.
Project application: In projects.py and users.py, database queries (e.g., db.query(Project).all()) are executed through SQLAlchemy's session (Session) object to perform create, read, update, and delete operations on project and user data and handle database exceptions (e.g., SQLAlchemyError).
3. JWT (JSON Web Token)
- Definition: An open standard (RFC 7519) for securely transmitting information between web applications. It is commonly used for user authentication and authorization, containing user information and expiration time. The token is signed to ensure its integrity.
Project application: In the login logic of users.py, a JWT token (create_access_token) is generated and returned to the client. Subsequent requests verify the user's identity through the token (verify_token) to achieve stateless authentication.
4. Controller
- Definition: In the MVC (Model - View - Controller) architecture, the controller is an intermediate layer that handles user requests, coordinates the model and the view. It is responsible for receiving input, invoking business logic, and returning responses.
Project application: projects.py and users.py in the controllers directory encapsulate business logic related to projects and users, such as data validation, database operations, and exception handling. They are the core modules connecting the routers and the models.
5. ORM (Object-Relational Mapping)
- Definition: A programming technique that maps database tables to objects in a programming language. It enables create, read, update, and delete operations on the database by manipulating objects, eliminating the need to write SQL statements directly, thus improving development efficiency and code maintainability.
Project application: In this project, the database table structure is defined through SQLAlchemy's ORM models (e.g., Project and User classes). Methods in the controller (e.g., get_all, create) perform database interactions by manipulating these objects. For example, db.add(new_item) corresponds to inserting a record into the database.
6. Dependency Injection
- Definition: A design pattern that passes dependencies (e.g., database sessions, configuration objects) to functions or classes instead of hard - coding them, improving code decoupling and testability.
Project application: FastAPI natively supports dependency injection. Controller functions (e.g., get_all(db: Session)) declare dependencies (e.g., db: Session) through parameters, and the framework automatically resolves and injects the database session, simplifying resource management.