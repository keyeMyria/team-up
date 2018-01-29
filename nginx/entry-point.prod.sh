#!/usr/bin/env bash
bash scripts/entry-point.sh

# Copy nginx configuration file
cp /etc/nginx/configurations/prod.nginx.conf /etc/nginx/conf.d/

# Wait until static files are ready
echo 'Static files not ready yet - waiting'
file=/opt/tu/static/ready
while [ ! -f ${file} ]
do
    inotifywait -qqt 2 -e create -e moved_to $(dirname ${file})
done
echo 'Static files ready'

# Remove auxiliary file
rm ${file}

# Run nginx
exec nginx -g 'daemon off;'
