# Worker C

Celery Worker C in microservices-based celery architecture.

# Project usage

Worker can be invoked (asynchronously) in two ways:

1. direct celery invocation:

```shell
celery call tasks.task_c --args='["arg_1", "arg_2", ...]' --kwargs='{"kwarg_1": kwarg_value, ...}'
```

2. via [Flower](../CeleryInfrastructure) REST API

```shell
curl -X POST --location 'http://localhost:8080/api/task/send-task/tasks.task_c' \
--header 'Content-Type: application/json' \
--data '{
    "args": ["arg_1", "arg_2", ...],
    "kwargs": {"kwarg_1": kwarg_value, ...}
}'
```

And so the check on task's status:

1. direct celery invocation:

```shell
celery result <taks-id>
```

2. via [Flower](../CeleryInfrastructure) REST API

```shell
curl --location '<backend-url>/flower/api/task/result/<taks-id>'
```

In order to see which _args_ and _kwargs_ are needed/possible check task implementation.

# Project setup (containerized)

## Prerequisites 

See main [README.md](../README.md)

## Environments

**Mind that all below commands can be run natively using docker-compose (not recommended, see _Makefile_ for details)**

<details>
<summary>Development Environment</summary>

### Prepare local environment

```shell
docker-compose --env-file=db.env.local build 
```

### Run local environment

```shell
docker-compose --env-file=db.env.local up -d
```

### Shut down and clean local environment

```shell
docker-compose --env-file=db.env.local down
```

</details>
</br>

## Useful commands

<details>
<summary>Uninstall all pip packages</summary>

```shell
pip freeze | xargs pip uninstall -y
```

</details>
</br>

## Notes

- [Celery Task Instantiation](https://docs.celeryq.dev/en/stable/userguide/tasks.html#instantiation)

---

[README.md](../README.md)
