FROM python:3.10

# install packages
RUN apt-get update
RUN apt-get install -y --no-install-recommends libatlas-base-dev gfortran nginx supervisor

COPY requirements.txt /
RUN pip install -r /requirements.txt

WORKDIR /app


ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

ENV GRAYLOG_IP=host.docker.internal
ENV GRAYLOG_PORT=12201

ENV ENVIRONMENT="dev"
ENV MYSQL_HOST=host.docker.internal
ENV MYSQL_PASSWORD=123456
ENV MYSQL_USER=user
ENV MYSQL_DB_NAME=fortune

COPY . .

WORKDIR /app/src

CMD [ "flask", "run"]