#!/usr/bin/env bash

docker build -t pef/mariadb:5.5 -f Dockerfile .
#docker build --build-arg DATABASE=$1 -t pef/mariadb:5.5 -f mariadb/Dockerfile .
#--name some-mariadb -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mariadb:tag