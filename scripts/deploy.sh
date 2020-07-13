#!/bin/bash

cvlc --play-and-exit /home/l31rb4g/deploy.ogg > /dev/null 2>&1 &

git add . && git commit -am go && git push origin master 

cvlc --play-and-exit /home/l31rb4g/over.ogg > /dev/null 2>&1
