#!/usr/bin/env bash
cd src

python manage.py migrate
touch /tmp/.done.info

exec sleep infinity
