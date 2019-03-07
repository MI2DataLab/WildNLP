FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y install \
    build-essential \
    python3-pip \
    python3-tk \
    python3.7 \
    python3.7-dev

RUN pip3 install --upgrade pip

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt