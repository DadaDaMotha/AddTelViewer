FROM python:3.7.0

ENV PYTHONUNBUFFERED 1

# Add a user
RUN groupadd --gid 1000 user \
&& useradd --uid 1000 --gid user --shell /bin/bash --create-home user

RUN mkdir -p /home/project/flask_app \
    && mkdir -p /scripts

WORKDIR /home/project/flask_app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# volume can be used to serve these files with a webserver
VOLUME /var/www/static
VOLUME /var/www/media

COPY --chown=user:user flaskapp .
COPY ./scripts/* /scripts/
RUN chmod -R u+x /scripts/*
EXPOSE 8080
# volume for live-reload during development, created in base image

# add gunicorn config
#COPY gunicorn.conf /etc/gunicorn/
# env can be overwritten by a compose file, this is default config
#ENV GUNICORN_WORKERS=2
#ENV GUNICORN_BIND=0.0.0.0:8000
#ENV GUNICORN_LOGLEVEL="warning"
#ENV GUNICORN_RELOAD="false"
#ENV FLASK_APP="run"
#COPY start.sh /
#RUN chmod +x /start.sh
#CMD ["/start.sh"]



