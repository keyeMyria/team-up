#!/usr/bin/env bash
# Prepare log files and start outputting logs to stdout
touch /opt/tu/logs/nginx/nginx-access.log
touch /opt/tu/logs/nginx/nginx-error.log
tail -n 0 -f /opt/tu/logs/nginx/*.log &

nginx -g 'daemon off;'
