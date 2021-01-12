#!/bin/bash
python manage.py migrate
# /bin/python3 /home/my-little-office/manage.py compilemessages
# /bin/python /home/my-little-office/manage.py collectstatic
# /home/my-little-office/.local/bin/gunicorn -w 4 my-little-office.wsgi --bind="0.0.0.0:8000"
python manage.py runserver 0.0.0.0:8000