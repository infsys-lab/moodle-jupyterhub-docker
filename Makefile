# Copyright (c) Atreya Shankar
# Distributed under the terms of the MIT License.
# Copyright (c) Jupyter Development Team
# Distributed under the terms of the Modified BSD License.

include .env
.PHONY: network volumes build up down restart log clean
.DEFAULT_GOAL=build

network:
	docker network inspect $(DOCKER_NETWORK_NAME) >/dev/null 2>&1 || docker network create $(DOCKER_NETWORK_NAME)

volumes:
	for volume in "$(JH_DATA_VOLUME_HOST)" \
	              "$(JH_DB_VOLUME_HOST)" \
	              "$(MOODLE_DB_VOLUME_HOST)" \
	              "$(MOODLE_MAIN_VOLUME_HOST)" \
	              "$(MOODLE_OTHER_VOLUME_HOST)"; do \
		docker volume create --name "$$volume"; \
	done

jupyterhub/secrets/postgres.env:
	@echo "Generating postgres password in $@"
	echo "POSTGRES_PASSWORD=$(shell openssl rand -hex 32)" > $@

jupyterhub/secrets/admins:
	@echo "Adding admin user '$(ADMIN)' to $@"
	echo "$(ADMIN)" > $@

jupyterhub/secrets/lti.key:
	@echo "Generating LTI client key in $@"
	echo "$(shell openssl rand -hex 32)" > $@

jupyterhub/secrets/lti.secret:
	@echo "Generating LTI shared secret in $@"
	echo "$(shell openssl rand -hex 32)" > $@

build: network volumes
build: jupyterhub/secrets/postgres.env jupyterhub/secrets/admins
build: jupyterhub/secrets/lti.key jupyterhub/secrets/lti.secret
	docker build -t $(LOCAL_NOTEBOOK_NAME) \
		--build-arg JUPYTERHUB_VERSION=$(JUPYTERHUB_VERSION) \
		--build-arg DOCKER_NOTEBOOK_IMAGE=$(DOCKER_NOTEBOOK_IMAGE) \
		singleuser
	docker-compose build
	docker image prune -f

up: build
	docker-compose up -d

down:
	docker-compose down

restart: down up

log:
	docker-compose logs -f -t

clean:
	-docker-compose down
	for volume in "$(JH_DATA_VOLUME_HOST)" \
	              "$(JH_DB_VOLUME_HOST)" \
	              "$(MOODLE_DB_VOLUME_HOST)" \
	              "$(MOODLE_MAIN_VOLUME_HOST)" \
	              "$(MOODLE_OTHER_VOLUME_HOST)"; do \
		docker volume rm -f "$$volume"; \
	done
	for volume in $$(docker volume ls --quiet | grep "jupyterhub-user"); do \
		docker volume rm -f "$$volume"; \
	done
	rm -f jupyterhub/secrets/*
