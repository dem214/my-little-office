import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_little_office.settings.dev')

app = Celery('my_little_office')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# This will edit schedule every time, if task not exist.
# If there are need to add task one time -- maybe this is good 
# reason to write this tsk in data migration
app.conf.beat_schedule = {
    'Accrue salary to all workers': {
        'task': 'my_little_office.apps.staff.tasks.accrue_salary',
        'schedule': timedelta(hours=2)
    },
}

