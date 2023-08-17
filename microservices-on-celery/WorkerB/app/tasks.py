import datetime

from celery_config import app, MAIN_QUEUE, MAIN_TASK, FOLLOWUP_TASK


@app.task(bind=True, name=MAIN_TASK, queue=MAIN_QUEUE)
def task_a(self, string: str, created: datetime.datetime, **kwargs) -> dict:
    """
    WorkerB's main task - parses dummy string to make it even dummier.
    """
    result = {
        "worker": self.request.hostname,
        "acknowledgeTime": datetime.datetime.now()
    }
    parsed_string = string.swapcase()

    follow_up_task = app.send_task(
        FOLLOWUP_TASK,
        args=[parsed_string, created],
        kwargs=kwargs,
        route_name=FOLLOWUP_TASK,
    )
    result["followUpTask"] = str(follow_up_task)
    return result
