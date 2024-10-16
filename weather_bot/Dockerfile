FROM python:3.12.4

WORKDIR /usr/src/weather_bot

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./weather_bot/requirements.txt .
RUN pip install -r requirements.txt

COPY . .