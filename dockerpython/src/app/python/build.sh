#!/usr/bin/env bash

docker build --add-host dockerhost:`docker network inspect --format='{{range .IPAM.Config}}{{.Gateway}}{{end}}' bridge`  -t pef/pefspikeapp:latest -f Dockerfile .
