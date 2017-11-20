#!/usr/bin/env bash

mkdir -p ~/pypi
docker run -ti --rm -h pypi.local -v ~/pypi:/srv/pypi:rw -p 8088:80 --name pypi pef/pypi
