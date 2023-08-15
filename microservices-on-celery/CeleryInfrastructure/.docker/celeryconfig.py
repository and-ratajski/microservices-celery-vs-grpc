# Please mind that if you won't specify queue for a task,
# it will be placed on the default 'celery' queue
task_routes = {
    "tasks.task_a": {
        "queue": "worker-a-queue",
    },
    "tasks.task_b": {
        "queue": "worker-b-queue",
    },
    "tasks.task_c": {
        "queue": "worker-c-queue",
    },
    "tasks.task_d": {
        "queue": "worker-d-queue",
    },
}
