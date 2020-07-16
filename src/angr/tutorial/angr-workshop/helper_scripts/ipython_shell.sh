#!/usr/bin/env bash
id=$(docker ps | grep angr-wo | awk '{ print $1 }')
docker exec -it -u angr "$id" jupyter-console --existing
