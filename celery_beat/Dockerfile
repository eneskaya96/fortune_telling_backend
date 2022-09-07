FROM python:3.10

# install packages
RUN apt-get update
RUN apt-get install -y --no-install-recommends libatlas-base-dev gfortran nginx supervisor


WORKDIR /app_celery
COPY . /app_celery

RUN pip install -r requirements.txt


ENV GRAYLOG_IP=host.docker.internal
ENV GRAYLOG_PORT=12201
ENV ENVIRONMENT="dev"
ENV AUTH_USERNAME=test
ENV AUTH_PASSWORD=test
ENV FORTUNE_API_URL=http://localhost:8000/
ENV BROKER_URL=amqp://user:123456@host.docker.internal:5672/

RUN chmod +777 start.sh

ENTRYPOINT ["./start.sh"]


