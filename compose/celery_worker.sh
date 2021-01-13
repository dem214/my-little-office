#!/bin/bash

celery -A my_little_office.celery worker -l INFO