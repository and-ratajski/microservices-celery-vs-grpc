#!/bin/bash

INFRASTRUCTURE="infrastructure-n-test-runner"
CELERY="microservices-on-celery"
CELERY_FLOWER="CeleryInfrastructure"
CELERY_WORKER_A="WorkerA"
CELERY_WORKER_B="WorkerB"
CELERY_WORKER_C="WorkerC"
CELERY_WORKER_D="WorkerD"

# Script accepts only one argument (mandatory)
if [ $# -ne 1 ]; then
	echo "Invalid argument number."
 	exit 1
fi

if [ "$1" = "build" ] || [ "$1" = "--build" ]; then
    echo ""
    echo "[INFO] Building local environment..."

    echo ""
    echo "[INFO] Building base infrastructure..."
    docker-compose --file $INFRASTRUCTURE/docker-compose.yml build

    echo ""
    echo "[INFO] Building Celery setup..."
    docker-compose --file $CELERY/$CELERY_FLOWER/docker-compose.yml --env-file $CELERY/$CELERY_FLOWER/.env.local build
    docker-compose --file $CELERY/$CELERY_WORKER_A/docker-compose.yml --env-file $CELERY/$CELERY_WORKER_A/.env.local build
    docker-compose --file $CELERY/$CELERY_WORKER_B/docker-compose.yml --env-file $CELERY/$CELERY_WORKER_B/.env.local build
    docker-compose --file $CELERY/$CELERY_WORKER_C/docker-compose.yml --env-file $CELERY/$CELERY_WORKER_C/.env.local build
    docker-compose --file $CELERY/$CELERY_WORKER_D/docker-compose.yml --env-file $CELERY/$CELERY_WORKER_D/.env.local build

    echo ""
    echo "[INFO] Local environment built!"

elif [ "$1" = "run" ] || [ "$1" = "--run" ]; then
    echo ""
    echo "[INFO] Starting local environment..."

    echo ""
    echo "[INFO] Starting base infrastructure..."
    docker-compose --file $INFRASTRUCTURE/docker-compose.yml up --detach

    echo ""
    echo "[INFO] Starting Celery setup..."
    docker-compose --file $CELERY/$CELERY_FLOWER/docker-compose.yml --env-file $CELERY/$CELERY_FLOWER/.env.local up --detach
    docker-compose --file $CELERY/$CELERY_WORKER_A/docker-compose.yml --env-file $CELERY/$CELERY_WORKER_A/.env.local up --detach
    docker-compose --file $CELERY/$CELERY_WORKER_B/docker-compose.yml --env-file $CELERY/$CELERY_WORKER_B/.env.local up --detach
    docker-compose --file $CELERY/$CELERY_WORKER_C/docker-compose.yml --env-file $CELERY/$CELERY_WORKER_C/.env.local up --detach
    docker-compose --file $CELERY/$CELERY_WORKER_D/docker-compose.yml --env-file $CELERY/$CELERY_WORKER_D/.env.local up --detach

    echo ""
    echo "[INFO] Local environment started!"

elif [ "$1" = "down" ] || [ "$1" = "--down" ]; then

    echo ""
    echo "[INFO] Destroying local environment..."

    echo ""
    echo "[INFO] Destroying Celery setup..."
    docker-compose --file $CELERY/$CELERY_FLOWER/docker-compose.yml --env-file $CELERY/$CELERY_FLOWER/.env.local down
    docker-compose --file $CELERY/$CELERY_WORKER_A/docker-compose.yml --env-file $CELERY/$CELERY_WORKER_A/.env.local down
    docker-compose --file $CELERY/$CELERY_WORKER_B/docker-compose.yml --env-file $CELERY/$CELERY_WORKER_B/.env.local down
    docker-compose --file $CELERY/$CELERY_WORKER_C/docker-compose.yml --env-file $CELERY/$CELERY_WORKER_C/.env.local down
    docker-compose --file $CELERY/$CELERY_WORKER_D/docker-compose.yml --env-file $CELERY/$CELERY_WORKER_D/.env.local down

    echo ""
    echo "[INFO] Destroying base infrastructure..."
    docker-compose --file $INFRASTRUCTURE/docker-compose.yml down

    echo ""
    echo "[INFO] Local environment downed!"

else
    echo "Invalid argument."
    exit 1

fi
