import datetime

from sqlalchemy.orm import Session

from db_config import db_session, TestString
from celery import Task

from celery_config import app, MAIN_QUEUE, MAIN_TASK
from sqlalchemy import text


class SqlAlchemyTask(Task):
    """
    An abstract Celery Task that ensures that the connection to the
    database is closed on task completion.
    """
    abstract = True

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        db_session.remove()


@app.task(base=SqlAlchemyTask, bind=True, name=MAIN_TASK, queue=MAIN_QUEUE)
def task_a(self, string: str, **kwargs) -> dict:
    """
    WorkerA's main task - parses dummy string to make it even dummier.
    """
    result = {
        "worker": self.request.hostname,
        "acknowledgeTime": datetime.datetime.now(),
    }
    # stmt = text(f"INSERT INTO {DB_TABLE} (x, y) VALUES (:x, :y)")
    # with engine.begin() as conn:
    #     conn.execute(stmt, [{"x": 11, "y": 12}, {"x": 13, "y": 14}])
    #     conn.commit()

    test_string = TestString(test_string=string)
    db_session.add(test_string)
    db_session.commit()

    return result
