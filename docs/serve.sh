#!/usr/bin/env sh
set -e

command -v docker

docker build -t svg .
docker run --rm --net=host --init --name svg -it svg:latest
