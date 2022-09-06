FROM python:3.10

# install packages
RUN apt-get update
RUN apt-get install -y --no-install-recommends libatlas-base-dev gfortran nginx supervisor

COPY ../requirements.txt /
RUN pip install -r ../requirements.txt

WORKDIR /app_celery


ENV GRAYLOG_IP=host.docker.internal
ENV GRAYLOG_PORT=12201

ENV ENVIRONMENT="dev"
ENV AUTH_USERNAME=test
ENV AUTH_PASSWORD=test

ENV FORTUNE_API_URL=http://localhost:8000/

ENV BROKER_URL=amqp://user:123456@localhost:15672/

COPY . .

WORKDIR /app

RUN celery -A src.worker beat -l INFO