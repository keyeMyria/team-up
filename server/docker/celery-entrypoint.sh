#!/usr/bin/env bash

# wait for RabbitMQ server to start
sleep 5

cd /opt/tu/celery/src
su -m myuser -c "celery -A config worker -l info"
