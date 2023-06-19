FROM python:3.11.4-bullseye

ENV PYTHONUNBUFFERED 1

RUN ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

WORKDIR /code 
COPY ./requirements.txt /code
RUN pip install -r requirements.txt
