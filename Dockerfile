FROM python:3.9

WORKDIR /home/

RUN git clone -b django --single-branch https://github.com/Jodayday/framework.git

WORKDIR /home/framework/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient


EXPOSE 8000

CMD ["bash","-c","python manage.py collectstatic --noinput --settings=config.settings.deploy && python manage.py migrate --settings=config.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=config.settings.deploy config.wsgi --bind 0.0.0.0:8000"]
