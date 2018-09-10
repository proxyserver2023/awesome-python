FROM python:3.6.4-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt