from celery import Celery

# Configure Celery with Redis as broker & backend
celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",   # Broker
    backend="redis://localhost:6379/0"   # Results
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="Asia/Kolkata",
    enable_utc=True,
)
