# Please mind that if you won't specify queue for a task,
# it will be placed on the default 'celery' queue
task_routes = {
    "tasks.worker_a": {
        "queue": "worker-a-queue",
    },
    "tasks.worker_b": {
        "queue": "worker-b-queue",
    },
    "tasks.worker_c": {
        "queue": "worker-c-queue",
    },
    "tasks.worker_d": {
        "queue": "worker-d-queue",
    },
}
