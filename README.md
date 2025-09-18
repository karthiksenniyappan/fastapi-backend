# FastAPI Project

This is a basic **FastAPI** project setup with support for:

- **Database** integration (via Tortoise ORM)
- **Security** (JWT)
- **Logging** (with log rotation, keeping only the last 5 days)
- **Celery** for background/long-running tasks
- **Redis** as the Celery broker
- **uv** for modern and fast Python package management

---

## 🚀 Features

- Fast and async Python web framework (**FastAPI**)
- Database support with migrations
- Authentication & Authorization
- Centralized logging
- Background task processing with Celery + Redis
- Environment-based configuration
- Docker-ready (optional)

---

## 📦 Installation

Install dependencies using uv

```shell
uv sync
```

## ⚙️ Configuration

Copy .env.example to .env and update values:

```shell
cp .env.example .env
```

## ▶️ Running the Application

Start the FastAPI server:

```shell
uv run server.py
```

Access the API docs:

- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc

## ⏳ Background Tasks with Celery

Start Celery worker:

```shell
uv run celery -A core.celery_worker.celery_app worker --loglevel=info --beat
```

## 📝 Logging

Logs are stored in the logs/ directory.

They are automatically rotated, keeping only the last 5 days of logs.

## 🗄 Database Migrations

Run migrations

```shell
python manage.py migrate
```

Create new migration:

```shell
python manage.py makemigrations
```

## 🐳 Docker (Optional)

Start radis server

```shell
 docker run -d -p 6379:6379 redis
```

## Run test

```shell
uv run pytest -v --disable-warnings
```

## 📌 To-Do

- Add CI/CD pipeline
- Add API versioning

## 🏁 License

MIT License. See `LICENSE` for details.