#!/bin/bash

DOCKER_ID=`docker run -d -p 5000:5000 app`
sleep 3

python3 app_test.py
EXIT_CODE=$?

docker stop $DOCKER_ID
docker rm $DOCKER_ID
exit $EXIT_CODE

