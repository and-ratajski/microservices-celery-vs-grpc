import os
from celery import Celery
import sys
from kombu import Exchange, Queue


def get_backend() -> str:
    """Build backend connection string based on passed env."""
    if os.environ.get("CELERY_BACKEND_TYPE") == "redis":
        _redis_host = os.environ.get("REDIS_HOST")
        _redis_port = os.environ.get("REDIS_PORT")
        _redis_pass = os.environ.get("REDIS_PASSWORD")
        return f"redis://:{_redis_pass}@{_redis_host}:{_redis_port}"
    else:
        sys.exit("Currently only redis result backend is supported.")


BROKER = os.environ.get("CELERY_BROKER_URL")
BACKEND = get_backend()
MAIN_QUEUE = os.environ.get("CELERY_MAIN_QUEUE")
MAIN_TASK = os.environ.get("CELERY_MAIN_TASK")
FOLLOWUP_QUEUE = os.environ.get("CELERY_FOLLOWUP_QUEUE")
FOLLOWUP_TASK = os.environ.get("CELERY_FOLLOWUP_TASK")


class Config(object):
    """Configuration class for the worker"""
    task_default_queue = MAIN_QUEUE
    task_default_exchange = MAIN_QUEUE
    task_default_exchange_type = "direct"
    task_default_routing_key = task_default_queue
    task_create_missing_queues = False
    task_acks_late = False  # set to True if you need late acknowledge (after work is done)


app = Celery("tasks", broker=BROKER, backend=BACKEND)
app.config_from_object(Config)


default_exchange = Exchange(
    app.conf.task_default_exchange, type=app.conf.task_default_exchange_type
)
default_queue = Queue(
    app.conf.task_default_queue,
    default_exchange,
    routing_key=app.conf.task_default_routing_key,
)
followup_exchange = Exchange(FOLLOWUP_QUEUE, type=app.conf.task_default_exchange_type)
followup_queue = Queue(
    FOLLOWUP_QUEUE,
    followup_exchange,
    routing_key=FOLLOWUP_QUEUE,
)
app.conf.task_queues = (
    default_queue,
    followup_queue,  # Include followup queue to worker but exclude it in startup command
)
app.conf.task_routes = {
    MAIN_TASK: {"queue": MAIN_QUEUE},
    FOLLOWUP_TASK: {"queue": FOLLOWUP_QUEUE},
}
