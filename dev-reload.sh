#!/usr/bin/env bash

if hash inotifywait 2>/dev/null; then
    inotifywait -e close_write -m -r . --exclude '(.git|.idea|node_modules)'|
    while read -r directory events filename; do
      if [[ "$directory" = ./nginx/* ]]; then
        echo "Reloading Nginx"
        make reload-nginx &
      fi
    done
else
    echo -e "\033[0;31mPlease run 'sudo apt install inotifywait' first!"
    exit 1
fi



