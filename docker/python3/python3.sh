#!/usr/bin/env bash

docker run -v $PWD/py:/code/py -it pef/python3 $*
