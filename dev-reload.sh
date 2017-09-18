#!/usr/bin/env bash

inotifywait -e close_write -m -r . --exclude '(.git|.idea|node_modules)'|
while read -r directory events filename; do
  if [[ "$directory" = ./nginx/* ]]; then
    echo "Reloading Nginx"
    make reload-nginx &
  fi
done
