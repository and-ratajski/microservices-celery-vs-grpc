import datetime

from db_config import test_table, engine
from celery import Task

from celery_config import app, MAIN_QUEUE, MAIN_TASK


class SqlAlchemyTask(Task):
    """
    An abstract Celery Task that ensures that the connection to the
    database is closed on task completion.
    """
    abstract = True

    def __init__(self) -> None:
        super().__init__()
        self.db_engine = engine


@app.task(base=SqlAlchemyTask, bind=True, name=MAIN_TASK, queue=MAIN_QUEUE)
def task_a(self, test_string: str, created: datetime.datetime, **kwargs) -> dict:
    """WorkerD's main task - saves string into DB."""
    _worker = self.request.hostname
    result = {
        "worker": _worker,
        "acknowledgeTime": datetime.datetime.now(),
    }

    with self.db_engine.begin() as conn:
        conn.execute(
            test_table.insert().values(
                test_string=test_string,
                worker=_worker,
                created=created,
            ),
        )

    return result
