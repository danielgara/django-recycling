# Project

## Run with Python

`python manage.py runserver`

## Run with Docker

`sudo docker build -t django-app .`

`sudo docker container run -d --name django-docker -p 80:80 django-app`

## Run with Docker Hub

`sudo docker run -d -p 80:80 --name django-recycling danielgara/django-recycling`
