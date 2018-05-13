#!/usr/bin/env bash

docker run -it -p 8888:8888 -v ${PWD}/src:/home/jovyan/work pef/jupyterlab_scipy $*
#docker run -it --network "host" -v ${PWD}/src:/home/jovyan/work pef/jupyterlab_scipy $*
