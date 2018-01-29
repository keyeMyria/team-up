#!/usr/bin/env bash
cd src

echo "Waiting for redis and postgres to start"
python wait_redis_postgres.py
python manage.py migrate

exec python manage.py runserver 0.0.0.0:8001
