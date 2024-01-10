FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /djangoproject3
COPY ./djangoproject3 /djangoproject3
WORKDIR /djangoproject3