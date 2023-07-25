import os
from celery import Celery
import datetime
import time
import random
import sys
from kombu import Exchange, Queue


def get_backend() -> str:
    """Build backend connection string based on passed env"""
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
    task_acks_late = True


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

random.seed()


@app.task(name=MAIN_TASK, queue=MAIN_QUEUE)
def bom_generate(
    name: str, description: str, project_levels_ids: list, pre_data: object, **kwargs
):
    """
    Main WorkerA task that generates BOM (Bill of Materials) for given
    assembly object or manual setup.

    :param name: name of BOM asset (only for database)
    :param description: description of BOM asset (only for database)
    :param project_levels_ids: project_levels to be linked with the BOM asset
        (only for database)
    :param pre_data: assembly object or manual setup
    :param kwargs: store_in_db: True|False
    :return: generated BOM in Celery Worker output format
    """
    if name == "reject":
        raise Exception("Rejection test")
    else:
        print("bom_generate start")
        print(pre_data)
        time.sleep(random.randint(0, 20))
        result = {
            "obj": name,
            "generationTime": datetime.datetime.now(),
            "generationVersion": os.environ.get("APP_VERSION", "x.x.x"),
        }
        if kwargs.get("store_in_db", False):
            follow_up_task = app.send_task(
                FOLLOWUP_TASK,
                args=[name, description, project_levels_ids, "BOM", result],
                route_name=FOLLOWUP_TASK,
            )
            result["followUpTask"] = str(follow_up_task)
        print("bom_generate stop")
        return result
