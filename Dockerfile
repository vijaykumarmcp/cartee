FROM python:3.7-slim
LABEL maintainer="vijaykumar"

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /cartee
WORKDIR /cartee
COPY ./cartee /cartee

RUN adduser user
USER user

EXPOSE 8000
