import datetime

from sqlalchemy.orm import Session

from celery_config import app, engine, MAIN_QUEUE, MAIN_TASK, DB_TABLE
from sqlalchemy import text


@app.task(bind=True, name=MAIN_TASK, queue=MAIN_QUEUE)
def task_a(self, string: str, **kwargs) -> dict:
    """
    WorkerA's main task - parses dummy string to make it even dummier.
    """
    result = {
        "worker": self.request.hostname,
        "acknowledgeTime": datetime.datetime.now()
    }
    stmt = text(f"INSERT INTO {DB_TABLE} (x, y) VALUES (:x, :y)")
    with engine.begin() as conn:
        conn.execute(stmt, [{"x": 11, "y": 12}, {"x": 13, "y": 14}])
        conn.commit()

    return result
