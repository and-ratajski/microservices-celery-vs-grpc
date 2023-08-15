MAKEFLAGS += --silent --keep-going

INFRASTRUCTURE = $(shell echo "infrastructure-n-test-runner")
CELERY = $(shell echo "microservices-on-celery")
CELERY_FLOWER = $(shell echo "CeleryInfrastructure")
CELERY_WORKER_A = $(shell echo "WorkerA")
CELERY_WORKER_B = $(shell echo "WorkerB")
CELERY_WORKER_C = $(shell echo "WorkerC")
CELERY_WORKER_D = $(shell echo "WorkerD")

OBJ_STORE = $(shell echo "ObjectStorage")
MAIN_BACK = $(shell echo "MainBackend")
FISCHER_DB = $(shell echo "FischerDBService")
CONNECTORS = $(shell echo "ConnectorCapacityService")
BOM = $(shell echo "BOMGeneratorWorker")
ASSETS = $(shell echo "AssetsService")


########################################################################################
####                               Local Environment                                ####
########################################################################################
.PHONY: build-local-env run-local-env down-local-env

# Build development environment
build-local-env:
	cd $(INFRASTRUCTURE) && docker-compose build
	cd $(CELERY)/$(CELERY_FLOWER) && docker-compose --env-file ./.env.local build
	cd $(CELERY)/$(CELERY_WORKER_A) && docker-compose --env-file ./.env.local build
	cd $(CELERY)/$(CELERY_WORKER_B) && docker-compose --env-file ./.env.local build
	cd $(CELERY)/$(CELERY_WORKER_C) && docker-compose --env-file ./.env.local build
	cd $(CELERY)/$(CELERY_WORKER_D) && docker-compose --env-file ./.env.local build

# Run local environment
run-local-env:
	cd $(INFRASTRUCTURE) && docker-compose up -d
	cd $(CELERY)/$(CELERY_FLOWER) && docker-compose --env-file ./.env.local up -d
	cd $(CELERY)/$(CELERY_WORKER_A) && docker-compose --env-file ./.env.local up -d
	cd $(CELERY)/$(CELERY_WORKER_B) && docker-compose --env-file ./.env.local up -d
	cd $(CELERY)/$(CELERY_WORKER_C) && docker-compose --env-file ./.env.local up -d
	cd $(CELERY)/$(CELERY_WORKER_D) && docker-compose --env-file ./.env.local up -d

# Down local environment
down-local-env:
	cd $(INFRASTRUCTURE) && docker-compose down
	cd $(CELERY)/$(CELERY_FLOWER) && docker-compose --env-file ./.env.local down
	cd $(CELERY)/$(CELERY_WORKER_A) && docker-compose --env-file ./.env.local down
	cd $(CELERY)/$(CELERY_WORKER_B) && docker-compose --env-file ./.env.local down
	cd $(CELERY)/$(CELERY_WORKER_C) && docker-compose --env-file ./.env.local down
	cd $(CELERY)/$(CELERY_WORKER_D) && docker-compose --env-file ./.env.local down