build-all:
	@make build-django
	@make build-postgres
	@make build-nginx
build-django:
	@docker-compose build tu-django
build-postgres:
	@docker-compose build tu-postgres
build-nginx:
	@docker-compose build tu-nginx

rebuild-all: clean-all build-all
rebuild-django: clean-django build-django
rebuild-postgres: clean-postgres build-postgres
rebuild-nginx: clean-nginx build-nginx

run-dev:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

run-dev-no-logs:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

migrate:
	@docker exec -t tu-django python server/src/manage.py migrate

# Containers and images ids
CONTS-POSTGRES=$(shell docker ps -a -q -f "name=tu-postgres")
CONTS-FLASK=$(shell docker ps -a -q -f "name=tu-django")
CONTS-NGINX=$(shell docker ps -a -q -f "name=tu-nginx")

#stop docker containers
stop-postgres:
	-@docker stop $(CONTS-POSTGRES)
stop-django:
	-@docker stop $(CONTS-FLASK)
stop-nginx:
	-@docker stop $(CONTS-NGINX)
stop:
	@docker-compose stop

#remove docker containers
rm-postgres:
	-@docker rm $(CONTS-POSTGRES)
rm-django:
	-@docker rm $(CONTS-FLASK)
rm-nginx:
	-@docker rm $(CONTS-NGINX)
rm: rm-postgres rm-django rm-nginx

# Remove volumes
rm-db-volume:
	-@docker volume rm db-data-volum
rm-nginx-volume:
	-@docker volume rm nginx-data-volume
rm-all-volumes: rm-db-volume rm-nginx-volume


#clean docker containers
clean-postgres: stop-postgres rm-postgres
clean-django: stop-django rm-django
clean-nginx: stop-nginx rm-nginx
clean-all: clean-postgres clean-django clean-nginx rm-all-volumes

#Open shell in container
shell-postgres:
	@docker exec -it tu-postgres bash
shell-django:
	@docker exec -it tu-django bash
shell-nginx:
	@docker exec -it tu-nginx bash

#Logs
logs:
	@docker-compose logs -f
logs-django:
	@docker logs -f tu-django
logs-postgres:
	@docker logs -f tu-postgres
logs-nginx:
	@docker logs -f tu-nginx

# reloads
# Only in dev mode local changes will be used after the reload
reload-nginx:
	@docker exec tu-nginx nginx -s reload
