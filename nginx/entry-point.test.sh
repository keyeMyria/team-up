#!/usr/bin/env bash
bash scripts/entry-point.sh

cp /etc/nginx/configurations/test.nginx.conf /etc/nginx/conf.d/

exec nginx -g 'daemon off;'
