FROM python:3.10

# install packages
RUN apt-get update
RUN apt-get install -y --no-install-recommends libatlas-base-dev gfortran nginx supervisor

COPY requirements.txt /
RUN pip install -r /requirements.txt

WORKDIR /code


ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
#ENV FLASK_RUN_PORT=5000
ENV FLASK_DEBUG=1


ENV MYSQL_HOST=172.23.0.1
ENV MYSQL_PASSWORD=123456
ENV MYSQL_USER=user
ENV MYSQL_DB_NAME=fortune

EXPOSE 5000
COPY . .
CMD [ "flask", "run"]

#CMD [ "python", "./start.py"]