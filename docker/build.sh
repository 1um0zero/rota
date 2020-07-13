#!/bin/bash

docker container rm rota

docker build . --no-cache -t rota

bash ./docker/run.sh
