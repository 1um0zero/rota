FROM alpine:3.9

RUN apk add --no-cache bash mysql-client python3 python3-dev build-base \
    mariadb-connector-c-dev sassc

RUN python3 -m ensurepip
