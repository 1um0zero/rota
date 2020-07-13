#!/bin/bash

./scripts/watcher.py &
cd src
./manage.py runserver
