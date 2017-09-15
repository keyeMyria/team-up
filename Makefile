# Bind build commands to proper mode
build-all: build-dev-all
build-redis: build-dev-redis
build-postgres: build-dev-postgres
build-django: build-dev-django
build-nginx: build-dev-nginx


# Build development containers
build-dev-all: build-redis build-postgres build-django build-nginx
build-dev-redis:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml build tu-redis
build-dev-postgres:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml build tu-postgres
build-dev-django:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml build tu-django
build-dev-nginx:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml build tu-nginx


# Build production containers
build-prod-all: build-prod-redis build-prod-postgres build-prod-django build-prod-nginx
build-prod-redis:
	@docker-compose -f docker-compose.yml build tu-redis
build-prod-postgres:
	@docker-compose -f docker-compose.yml build tu-postgres
build-prod-django:
	@docker-compose -f docker-compose.yml build tu-django
build-prod-nginx:
	@docker-compose -f docker-compose.yml build tu-nginx


# Rebuild docker containers - stop -> remove -> build
rebuild-all: clean-all build-all
rebuild-redis: clean-redis build-redis
rebuild-postgres: clean-postgres build-postgres
rebuild-django: clean-django build-django
rebuild-nginx: clean-nginx build-nginx


run-dev:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

run-dev-no-logs:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

migrate:
	@docker exec -t tu-django python src/manage.py migrate


# Containers and images ids
ID-REDIS=$(shell docker ps -a -q -f "name=tu-redis")
ID-POSTGRES=$(shell docker ps -a -q -f "name=tu-postgres")
ID-DJANGO=$(shell docker ps -a -q -f "name=tu-django")
ID-NGINX=$(shell docker ps -a -q -f "name=tu-nginx")


# Stop docker containers
stop-redis:
	-@docker stop $(ID-REDIS)
stop-postgres:
	-@docker stop $(ID-POSTGRES)
stop-django:
	-@docker stop $(ID-DJANGO)
stop-nginx:
	-@docker stop $(ID-NGINX)
stop:
	@docker-compose stop


# Remove docker containers
rm-redis:
	-@docker rm $(ID-REDIS)
rm-postgres:
	-@docker rm $(ID-POSTGRES)
rm-django:
	-@docker rm $(ID-DJANGO)
rm-nginx:
	-@docker rm $(ID-NGINX)
rm: rm-nginx rm-django rm-postgres rm-redis


# Remove volumes
rm-db-volume:
	@docker volume rm teamupserver_db-data-volume
rm-nginx-volume:
	-@docker volume rm teamupserver_nginx-data-volume
rm-all-volumes: rm-db-volume rm-nginx-volume


# Clean docker containers
clean-redis: stop-redis rm-redis
clean-postgres: stop-postgres rm-postgres
clean-django: stop-django rm-django
clean-nginx: stop-nginx rm-nginx
clean-all: clean-nginx clean-django clean-postgres clean-redis rm-all-volumes


# Open shell in container
shell-redis:
	@docker exec -it tu-redis bash
shell-postgres:
	@docker exec -it tu-postgres bash
shell-django:
	@docker exec -it tu-django bash
shell-nginx:
	@docker exec -it tu-nginx bash


# Logs
logs:
	@docker-compose logs -f
logs-redis:
	@docker logs -f tu-redis
logs-postgres:
	@docker logs -f tu-postgres
logs-django:
	@docker logs -f tu-django
logs-nginx:
	@docker logs -f tu-nginx


# Tests
# Starts containers so that we are ready to run tests in them
prepare-tests:
	-@docker-compose -f docker-compose.yml -f docker-compose.test.yml up -d
# Run tests
test:
	@docker exec -t tu-django pytest src/


# Reloads
# Only in dev mode local changes will be used after the reload
reload-nginx:
	@docker exec tu-nginx nginx -s reload
