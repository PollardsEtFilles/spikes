#!/usr/bin/env bash

htpasswd -cb htpasswd ${USER} password
docker build -t pef/pypi:latest -f Dockerfile .
