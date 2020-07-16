#!/usr/bin/env sh
docker run -d -it --user angr -w /home/angr -v $(pwd):/home/angr/hostcwd -p 8888:8888 angr-workshop:latest jupyter-notebook --ip 0.0.0.0

sleep 1
id=$(docker ps | grep angr-wo | awk '{ print $1 }')
docker exec -it -u angr "$id" jupyter notebook list 

docker attach "$id"
