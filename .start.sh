#!/bin/bash
python manage.py migrate
# /bin/python /home/my-little-office/manage.py collectstatic
python manage.py compilemessages --ignore="venv/*"
python manage.py runserver 0.0.0.0:8000