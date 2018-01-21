#!/usr/bin/env bash

htpasswd -cb htpasswd ${USER} password
docker build -t pef/pypi:1.0.0 -f Dockerfile .
