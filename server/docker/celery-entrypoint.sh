#!/usr/bin/env bash

# wait for RabbitMQ server to start
sleep 5

cd /opt/tu/celery/src
exec su -m myuser -c "celery -A config worker -l info"
