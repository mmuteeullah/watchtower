#!/bin/bash

docker build -t watctower:test -f Dockerfile.test .
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock watctower:test