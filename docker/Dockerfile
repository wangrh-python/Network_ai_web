FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Asia/Shanghai

RUN apt-get update && \
    apt-get install -y tzdata \
    build-essential \
    git \
    vim \
    openssl \
    libssl-dev \
    libssl1.1 \ 
    python3-pip \
    python3 \
    python3-dev \
    default-libmysqlclient-dev \
    && cp /usr/bin/python3.8 /usr/bin/python \
    && dpkg-reconfigure tzdata

RUN pip3 install --upgrade pip && \
    pip3 install Django==3.2 \
    mysqlclient

