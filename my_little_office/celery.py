import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_little_office.settings.dev')

app = Celery('my_little_office')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()