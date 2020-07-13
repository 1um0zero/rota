#!/bin/bash

docker run \
    --rm \
    --name rota \
    -v $(pwd):/app \
    -p 8888:8888 \
    -it rota \
    bash /app/docker/exec.sh
