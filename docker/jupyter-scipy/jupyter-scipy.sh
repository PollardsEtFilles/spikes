#!/usr/bin/env bash

docker run -v $PWD/py:/code/py -it --rm -p 8888:8888 pef/jupyter-scipy $*
