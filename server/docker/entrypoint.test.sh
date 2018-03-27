#!/usr/bin/env bash
cd src

python manage.py migrate
python wait_redis_postgres.py

touch /tmp/.done.info

daphne -p 8001 config.asgi:application
