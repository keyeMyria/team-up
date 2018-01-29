#!/usr/bin/env bash
cd src

python manage.py migrate
exec sleep infinity
