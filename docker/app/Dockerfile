FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

RUN pip install --upgrade pip
COPY djangoBaseGB/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
