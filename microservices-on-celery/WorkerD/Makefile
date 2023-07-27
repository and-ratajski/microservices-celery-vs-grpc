MAKEFLAGS += --silent --keep-going
APP_NAME = $(shell echo "WorkerA")
ENV_FILE = $(shell echo "./.env.local")
DOCKER_COMPOSE_FILE = $(shell echo "docker-compose.yml")


########################################################################################
####                               Local Environment                                ####
########################################################################################
.PHONY: build-dev-env run-dev-env down-dev-env
.PHONY: run-unit-tests run-ut-coverage-html

# Build DEV instance
build-dev-env:
	@docker-compose \
 		--file $(DOCKER_COMPOSE_FILE) \
 		build
	@echo "[INFO] $(APP_NAME) dev images were successfully built"

# Run DEV instance
run-dev-env:
	@docker-compose \
		--file $(DOCKER_COMPOSE_FILE) up \
		--detach
	@echo "[INFO] $(APP_NAME) dev services were successfully started!"

# Stop and clear DEV instance
down-dev-env:
	@docker-compose \
		--file $(DOCKER_COMPOSE_FILE) \
 		down \
 		--remove-orphans
	@echo "[INFO] $(APP_NAME) dev services were successfully downed."
