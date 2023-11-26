FROM ubuntu:latest
LABEL authors="pastrychef"

ENTRYPOINT ["top", "-b"]