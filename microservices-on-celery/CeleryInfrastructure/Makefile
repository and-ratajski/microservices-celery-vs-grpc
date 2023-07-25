MAKEFLAGS += --silent --keep-going
APP_NAME = $(shell echo "Celery Infrastructure")
ENV_FILE = $(shell echo "./.env.local")
DOCKER_COMPOSE = $(shell echo "docker-compose.yml")


########################################################################################
####                               Local Environment                                ####
########################################################################################
.PHONY: build-dev-env run-dev-env down-dev-env

# Build DEV images
build-dev-env:
	@docker-compose \
 		--file $(DOCKER_COMPOSE_DEV) \
		--env-file flower.env.local \
 		build
	@echo "[INFO] $(APP_NAME) dev images were successfully built"

# Run DEV services
run-dev-env:
	@docker-compose \
		--file $(DOCKER_COMPOSE_DEV) \
		--env-file flower.env.local \
		up \
		--detach
	@echo "[INFO] $(APP_NAME) dev services were successfully started!"

# Stop and clear DEV services
down-dev-env:
	@docker-compose \
		--file $(DOCKER_COMPOSE_DEV) \
		--env-file flower.env.local \
 		down \
 		--remove-orphans
	@echo "[INFO] $(APP_NAME) dev services were successfully downed."

