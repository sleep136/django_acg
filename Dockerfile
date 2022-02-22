FROM python:3.6-jessie

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -i https://pypi.doubanio.com/simple -r requirements.txt

COPY . /usr/src/app

RUN python3 manage.py collectstatic --noinput



CMD ["/usr/local/bin/gunicorn", "haid_project.wsgi:application", "-w", "6", "-b", "0.0.0.0:8000" ]

EXPOSE 8000