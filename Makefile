# Bind build commands to proper mode
build-all: build-dev-all
build-redis: build-dev-redis
build-postgres: build-dev-postgres
build-django: build-dev-django
build-nginx: build-dev-nginx
build-react: build-dev-react
build-rabbitmq: build-dev-rabbitmq
build-celery: build-dev-celery


# Build development containers
build-dev-all: build-dev-redis build-dev-postgres build-dev-django build-dev-nginx build-dev-react build-dev-rabbitmq build-dev-celery
build-dev-redis:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml build tu-redis
build-dev-postgres:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml build tu-postgres
build-dev-django:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml build tu-django
build-dev-nginx:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml build tu-nginx
build-dev-react:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml build tu-react
build-dev-rabbitmq:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml build tu-rabbitmq
build-dev-celery:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml build tu-celery


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
build-prod-rabbitmq:
	@docker-compose -f docker-compose.yml build tu-rabbitmq
build-prod-celery:
	@docker-compose -f docker-compose.yml build tu-celery


# Rebuild docker containers - stop -> remove -> build
rebuild-all: clean-all build-all
rebuild-redis: clean-redis build-redis
rebuild-postgres: clean-postgres build-postgres
rebuild-django: clean-django build-django
rebuild-nginx: clean-nginx build-nginx
rebuild-react: clean-react build-react
rebuild-rabbitmq: clean-rabbitmq build-rabbitmq
rebuild-celery: clean-celery build-celery


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
ID-REACT=$(shell docker ps -a -q -f "name=tu-react")
ID-RABBITMQ=$(shell docker ps -a -q -f "name=tu-rabbitmq")
ID-CELERY=$(shell docker ps -a -q -f "name=tu-celery")


# Stop docker containers
stop-redis:
	-@docker stop $(ID-REDIS)
stop-postgres:
	-@docker stop $(ID-POSTGRES)
stop-django:
	-@docker stop $(ID-DJANGO)
stop-nginx:
	-@docker stop $(ID-NGINX)
stop-react:
	-@docker stop $(ID-REACT)
stop-rabbitmq:
	-@docker stop $(ID-RABBITMQ)
stop-celery:
	-@docker stop $(ID-CELERY)
stop:
	@docker-compose stop


# Remove docker containers
rm-redis:
	-@docker rm --volumes $(ID-REDIS)
rm-postgres:
	-@docker rm --volumes $(ID-POSTGRES)
rm-django:
	-@docker rm --volumes $(ID-DJANGO)
rm-nginx:
	-@docker rm --volumes $(ID-NGINX)
rm-react:
	-@docker rm --volumes $(ID-REACT)
rm-rabbitmq:
	-@docker rm --volumes $(ID-RABBITMQ)
rm-celery:
	-@docker rm --volumes $(ID-CELERY)
rm: rm-nginx rm-django rm-postgres rm-redis rm-rabbitmq rm-celery rm-react


# Remove volumes
rm-db-volume:
	@docker volume rm teamup_db-data-volume
rm-nginx-volume:
	-@docker volume rm teamup_nginx-data-volume
rm-static-volume:
	-@docker volume rm teamup_static-volume

rm-all-volumes: rm-db-volume rm-nginx-volume rm-static-volume


# Clean docker containers
clean-redis: stop-redis rm-redis
clean-postgres: stop-postgres rm-postgres
clean-django: stop-django rm-django
clean-nginx: stop-nginx rm-nginx
clean-react: stop-react rm-react
clean-rabbitmq: stop-rabbitmq rm-rabbitmq
clean-celery: stop-celery rm-celery
clean-all: clean-nginx clean-django clean-postgres clean-redis clean-rabbitmq clean-celery \
			clean-react rm-all-volumes


# Open shell in container
shell-redis:
	@docker exec -it tu-redis bash
shell-postgres:
	@docker exec -it tu-postgres bash
shell-django:
	@docker exec -it tu-django bash
shell-nginx:
	@docker exec -it tu-nginx bash
shell-react:
	@docker exec -it tu-react bash
shell-celery:
	@docker exec -it tu-celery bash


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
logs-rabbitmq:
	@docker logs -f tu-rabbitmq
logs-celery:
	@docker logs -f tu-celery


# utils
dev-reload:
	@bash dev-reload.sh
createsu:
	@docker exec tu-django python src/manage.py createsu
monitor-dying:
	@docker events --filter event=die --format '{{.Type}} {{.Actor.Attributes.name}} died'\
	'- exitcode: {{.Actor.Attributes.exitCode}}' | grep -ivE '(?exit|code).*0'

# Tests
# Starts containers so that we are ready to run tests in them
prepare-tests:
	-@docker-compose -f docker-compose.yml -f docker-compose.test.yml up -d
# Run tests
test:
	@docker exec -t tu-django bash -c "PYTHONDONTWRITEBYTECODE=1 pytest src/"
	@docker exec -t tu-react bash -c "CI=true npm test"


# Reloads
# Only in dev mode local changes will be used after the reload
reload-nginx:
	@docker exec tu-nginx nginx -s reload
