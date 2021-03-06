#!/bin/sh
cd /app

if [ $# -eq 0 ]; then
  nginx
  gunicorn haid_project.wsgi:application \
    --name haid_backend \
    --user root \
    --group root \
    --bind 127.0.0.1:8000 \
    --log-level=debug \
    --log-file=- \
    --workers $(grep -c ^processor /proc/cpuinfo) \
    --worker-class gevent
else
  python3 ./manage.py $1
fi
