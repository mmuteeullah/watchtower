#!/bin/bash

bash run_test.sh # Execute test script

if [ $? -eq 0 ]; then
    docker build -t watctower:prod -f Dockerfile .
    docker run --rm -p 80:8080 -v /var/run/docker.sock:/var/run/docker.sock --network watchtower-network watctower:prod
else
    echo "Test Failed"
    exit 1
fi
