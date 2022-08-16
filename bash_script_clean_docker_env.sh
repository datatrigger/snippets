#!/bin/bash

cd ~/path/to/docker_directory
docker build -t registry/image .
docker push registry/image

docker stop $(docker ps -q)
docker rm $(docker ps -aq)
docker volume rm $(docker volume ls -q)