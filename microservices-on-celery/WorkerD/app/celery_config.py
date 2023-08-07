import os
import sys
import re

from celery import Celery
from celery.signals import worker_init
from kombu import Exchange, Queue
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, UUID, TIMESTAMP


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

DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_NAME = os.environ.get("POSTGRES_DB")
DB_TABLE = os.environ.get("DB_TABLE")
engine = create_engine(f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")


@worker_init.connect
def init_db(sender=None, **kwargs) -> None:
    """Connects to DB and creates testing table on worker init."""
    worker_pattern = re.compile("worker-d@")
    if worker_pattern.match(str(sender)):
        metadata_obj = MetaData()
        celery_table = Table(
            DB_TABLE,
            metadata_obj,
            Column("id", UUID, primary_key=True),
            Column("test_string", String(8192), nullable=False),
            Column("worker", String(64), nullable=False),
            Column("requested", TIMESTAMP, nullable=False),
            Column("added", TIMESTAMP, nullable=False)
        )

        metadata_obj.create_all(engine)

        with engine.begin() as conn:
            conn.execute(text(f"CREATE TABLE {DB_TABLE} (x int, y int)"))
        # with engine.connect() as conn:
        #     conn.execute(text(f"CREATE TABLE {DB_TABLE} (x int, y int)"))
        #     conn.commit()
