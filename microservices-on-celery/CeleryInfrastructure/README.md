# Celery Flower Service 

This service palys two roles:

1. Celery task producer exposing REST API
2. Monitoring tool with GUI for Celery infrastructure 

# Project usage

1. How to use Flower REST API is described in [official documentation](https://flower.readthedocs.io/en/latest/api.html)
2. There are two monitoring options available:
    * using build-in Flower GUI under `/flower` endpoint
    * scraping metrics in Prometheus and viewing them in Grafana. More info [here](https://flower.readthedocs.io/en/latest/prometheus-integration.html#celery-flower-prometheus-grafana-integration-guide). Grafana dashboard definition: [celery-monitoring-grafana-dashboard.json](./celery-monitoring-grafana-dashboard.json)

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

## Usefull links

* [Celery](https://docs.celeryq.dev/en/latest/index.html#)
* [Celery task](https://docs.celeryq.dev/en/latest/userguide/tasks.html)

---

[README.md](../README.md)
