# BOM Generator Worker

**CURRENT STATUS** under development

TODOs:

* actual implementation
* centralized logging

# Project usage

Worker can be invoked (asynchronously) in two ways:

1. direct celery invocation:

```shell
celery call tasks.bom_generate --args='["arg_1", "arg_2", ...]' --kwargs='{"kwarg_1": kwarg_value, ...}'
```

2. via [Flower](../CeleryInfrastructure) REST API

```shell
curl --location '<backend-url>/flower/api/task/send-task/tasks.bom_generate' \
--header 'Authorization: Bearer <token>' \
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
curl --location '<backend-url>/flower/api/task/result/<taks-id>' \
--header 'Authorization: Bearer <token>'
```

In order to see which _args_ and _kwargs_ are needed/possible check task implementation.

# Project setup (containerized)

## Prerequisites 

1. [docker](https://docs.docker.com/get-docker/)
2. [docker-compose](https://docs.docker.com/compose/install/)
3. [Optional & <u>HIGHLY</u> Recommended] **GNU make** (see below)

### GNU make - Make use of _Makefile_

It is recommended to make use of _make_ commands and in order to do so install *GNU make*

* Unix/Linux -> ready-to-go [more info](https://makefiletutorial.com/#running-the-examples)
* Windows (Powershell) -> [install chocolatey](https://chocolatey.org/install) and then run `choco install make` in **Powershell**
* MacOS -> for most recent versions you should be ready-to-go, if not try installing it with [homebrew](https://formulae.brew.sh/formula/make)


## Environments

**Mind that all below commands can be run natively using docker-compose (not recommended, see _Makefile_ for details)**

<details>
<summary>Development Environment</summary>

### Prepare development environment

```shell
make build-dev-env
```

### Run development environment

```shell
make run-dev-env
```

### See application logs

```shell
make attach-dev-env
```

### Shut down and clean development environment

```
make down-dev-env
```

</details>
</br>

<details>
<summary>Staging Environment</summary>

Please mind that all staging deployments are handled by a deployment script. You should
find more info under [deployment](../README.md#deployment)

</details>
</br>

<details>
<summary>Production Environment</summary>

Analogous to **Staging Environment** if not decided otherwise.

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
