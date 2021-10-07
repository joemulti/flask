#!/bin/bash

docker network inspect appnet

if [[ $? -ne 0 ]]; then
    docker network create --subnet=172.20.0.0/24 --gateway=172.20.0.1 appnet
fi

DOCKER_LB_ID=`docker run --net appnet --ip 172.20.0.10 -p 8282:8282 -itd registry-cido.experteach.demo:1234/root/application/lb`
DOCKER_APP1_ID=`docker run --net appnet --ip 172.20.0.100 -itd registry-cido.experteach.demo:1234/root/application/app`
DOCKER_APP2_ID=`docker run --net appnet --ip 172.20.0.101 -itd registry-cido.experteach.demo:1234/root/application/app`
sleep 5

python3 system_tests.py
EXIT_CODE=$?

docker stop $DOCKER_LB_ID
docker rm $DOCKER_LB_ID
docker stop $DOCKER_APP1_ID
docker rm $DOCKER_APP1_ID
docker stop $DOCKER_APP2_ID
docker rm $DOCKER_APP2_ID
docker network rm appnet
exit $EXIT_CODE

