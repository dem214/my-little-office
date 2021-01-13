#!/bin/bash

celery -A my_little_office beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler