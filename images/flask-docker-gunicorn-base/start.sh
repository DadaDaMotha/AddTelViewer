#!/usr/bin/env bash
set -e
# start gunicorn
echo "exec-starting gunicorn at ${GUNICORN_BIND} (RELOAD=${GUNICORN_RELOAD}, APP=${FLASK_APP})"
# gunicorn.conf adds env vars from docker to python for gunicorn (BIND, RELOAD).
#exec gunicorn -c /etc/gunicorn/gunicorn.conf run:server
#exec gunicorn -c /etc/gunicorn/gunicorn.conf ${FLASK_APP}:flask_server
exec gunicorn -c /etc/gunicorn/gunicorn.conf wsgi:flask_server
