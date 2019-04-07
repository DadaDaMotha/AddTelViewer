# images/flask-docker-gunicorn-base/Dockerfile
FROM python:3.7.0
MAINTAINER dadadamotha@gmail.com
LABEL dockerfile_location="" \
      image_name=flask-docker-gunicorn-base \
      base_image=python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /var/www/static && mkdir -p /var/www/media && mkdir -p /etc/gunicorn && mkdir -p /home/project/flask_app
WORKDIR /home/project/flask_app
COPY base-requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r base-requirements.txt

# volume can be used to serve these files with a webserver
VOLUME /var/www/static
VOLUME /var/www/media
# volume for live-reload during development, created in base image

# add gunicorn config
COPY gunicorn.conf /etc/gunicorn/
# env can be overwritten by a compose file, this is default config
ENV GUNICORN_WORKERS=2
ENV GUNICORN_BIND=0.0.0.0:8000
ENV GUNICORN_LOGLEVEL="warning"
ENV GUNICORN_RELOAD="false"
ENV FLASK_APP="run"
COPY start.sh /
RUN chmod +x /start.sh
CMD ["/start.sh"]


