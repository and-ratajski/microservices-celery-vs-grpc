# Celery Flower Service 

This service (Flower) plays two roles:

1. Celery task producer exposing REST API
2. Monitoring tool with GUI for Celery infrastructure 

The celery infrastructure itself uses:

1. [RabbitMQ](https://www.rabbitmq.com/) as message broker
2. [Redis](https://redis.io/) as (intermittent) result backend

# Project usage

1. How to use Flower REST API is described in [official documentation](https://flower.readthedocs.io/en/latest/api.html)
2. There are two monitoring options available:
    * using build-in Flower GUI on [http://127.0.0.1:8080](http://127.0.0.1:8080) 
    * scraping metrics in Prometheus and viewing them in Grafana. More info [here](https://flower.readthedocs.io/en/latest/prometheus-integration.html#celery-flower-prometheus-grafana-integration-guide). Grafana dashboard definition: [celery-monitoring-grafana-dashboard.json](./celery-monitoring-grafana-dashboard.json)

## Environments

<details>
<summary>Local Environment</summary>

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


## Useful links

* [Celery](https://docs.celeryq.dev/en/latest/index.html#)
* [Celery task](https://docs.celeryq.dev/en/latest/userguide/tasks.html)

---

[README.md](../README.md)
