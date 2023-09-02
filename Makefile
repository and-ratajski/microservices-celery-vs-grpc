MAKEFLAGS += --silent --keep-going

DB = $(shell echo "database")
CELERY = $(shell echo "microservices-on-celery")
CELERY_FLOWER = $(shell echo "CeleryInfrastructure")
CELERY_WORKER_A = $(shell echo "WorkerA")
CELERY_WORKER_B = $(shell echo "WorkerB")
CELERY_WORKER_C = $(shell echo "WorkerC")
CELERY_WORKER_D = $(shell echo "WorkerD")

GRPC = $(shell echo "microservices-with-grpc")
GRPC_SERVICE_A = $(shell echo "ServiceA")
GRPC_SERVICE_B = $(shell echo "ServiceB")
GRPC_SERVICE_C = $(shell echo "ServiceC")
GRPC_SERVICE_D = $(shell echo "ServiceD")

########################################################################################
####                               Local Environment                                ####
########################################################################################
.PHONY: build-local-env run-local-env down-local-env

# Build development environment
build-local-env:
	cd $(DB) && docker-compose build

	cd $(CELERY)/$(CELERY_FLOWER) && docker-compose --env-file ./.env.local build
	cd $(CELERY)/$(CELERY_WORKER_A) && docker-compose --env-file ./.env.local build
	cd $(CELERY)/$(CELERY_WORKER_B) && docker-compose --env-file ./.env.local build
	cd $(CELERY)/$(CELERY_WORKER_C) && docker-compose --env-file ./.env.local build
	cd $(CELERY)/$(CELERY_WORKER_D) && docker-compose --env-file ./.env.local build

	cd $(GRPC)/$(GRPC_SERVICE_D) && docker-compose --env-file ./.env.local build
	cd $(GRPC)/$(GRPC_SERVICE_C) && docker-compose --env-file ./.env.local build
	cd $(GRPC)/$(GRPC_SERVICE_B) && docker-compose --env-file ./.env.local build
	cd $(GRPC)/$(GRPC_SERVICE_A) && docker-compose --env-file ./.env.local build

# Run local environment
run-local-env:
	cd $(DB) && docker-compose up -d

	cd $(CELERY)/$(CELERY_FLOWER) && docker-compose --env-file ./.env.local up -d
	cd $(CELERY)/$(CELERY_WORKER_A) && docker-compose --env-file ./.env.local up -d
	cd $(CELERY)/$(CELERY_WORKER_B) && docker-compose --env-file ./.env.local up -d
	cd $(CELERY)/$(CELERY_WORKER_C) && docker-compose --env-file ./.env.local up -d
	cd $(CELERY)/$(CELERY_WORKER_D) && docker-compose --env-file ./.env.local up -d

	cd $(GRPC)/$(GRPC_SERVICE_D) && docker-compose --env-file ./.env.local up -d
	cd $(GRPC)/$(GRPC_SERVICE_C) && docker-compose --env-file ./.env.local up -d
	cd $(GRPC)/$(GRPC_SERVICE_B) && docker-compose --env-file ./.env.local up -d
	cd $(GRPC)/$(GRPC_SERVICE_A) && docker-compose --env-file ./.env.local up -d

# Down local environment
down-local-env:
	cd $(GRPC)/$(GRPC_SERVICE_D) && docker-compose --env-file ./.env.local down
	cd $(GRPC)/$(GRPC_SERVICE_C) && docker-compose --env-file ./.env.local down
	cd $(GRPC)/$(GRPC_SERVICE_B) && docker-compose --env-file ./.env.local down
	cd $(GRPC)/$(GRPC_SERVICE_A) && docker-compose --env-file ./.env.local down

	cd $(CELERY)/$(CELERY_WORKER_A) && docker-compose --env-file ./.env.local down
	cd $(CELERY)/$(CELERY_WORKER_B) && docker-compose --env-file ./.env.local down
	cd $(CELERY)/$(CELERY_WORKER_C) && docker-compose --env-file ./.env.local down
	cd $(CELERY)/$(CELERY_WORKER_D) && docker-compose --env-file ./.env.local down
	cd $(CELERY)/$(CELERY_FLOWER) && docker-compose --env-file ./.env.local down

    cd $(DB) && docker-compose down
