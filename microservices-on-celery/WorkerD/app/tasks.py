import datetime

from db_config import db_session, TestTable
from celery import Task

from celery_config import app, MAIN_QUEUE, MAIN_TASK


class SqlAlchemyTask(Task):
    """
    An abstract Celery Task that ensures that the connection to the
    database is closed on task completion.
    """
    abstract = True

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        db_session.remove()


@app.task(base=SqlAlchemyTask, bind=True, name=MAIN_TASK, queue=MAIN_QUEUE)
def task_a(self, string: str, created: datetime.datetime, **kwargs) -> dict:
    """WorkerD's main task - saves string into DB."""
    _worker = self.request.hostname
    result = {
        "worker": _worker,
        "acknowledgeTime": datetime.datetime.now(),
    }
    db_session.add(TestTable(test_string=string, worker=_worker, created=created))
    db_session.commit()

    return result
