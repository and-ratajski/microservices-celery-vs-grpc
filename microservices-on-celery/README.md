# Microservices-based architecture built upon Celery framework

# Project setup (containerized)

## Prerequisites 

1. [docker](https://docs.docker.com/get-docker/)
2. [docker-compose](https://docs.docker.com/compose/install/)
3. docker external network (see below)

## Prepare docker external network

Create docker external network if not already created

```shell
docker network create celery-vs-grpc-local 
```
