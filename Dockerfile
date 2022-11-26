# syntax=docker/dockerfile:1

FROM python:3.10-rc-slim-buster

WORKDIR /it-project

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:80