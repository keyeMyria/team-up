#!/usr/bin/env bash
cd src

echo "Waiting for redis and postgres to start"
python wait_redis_postgres.py
python manage.py migrate

echo "from django.contrib.auth import get_user_model;get_user_model().objects.create_superuser('admin', 'admin@admin.com', 'admin') if not get_user_model().objects.filter(username='admin').exists() else print('admin already created')" | python manage.py shell


exec python manage.py runserver 0.0.0.0:8001
