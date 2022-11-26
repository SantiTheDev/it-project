# syntax=docker/dockerfile:1

FROM python:3.10-rc-slim-buster

WORKDIR /it-project

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Installing dependencies
RUN pip3 install gunicorn

COPY . .

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver