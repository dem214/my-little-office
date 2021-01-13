from django.db.models import F

from my_little_office.celery import app
from .models import Employee


def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, accrue_salary.s())


@app.task
def accrue_salary():
    Employee.objects.update(total_accrued=F('total_accrued')+F('salary'))


@app.task
def clean_total_accrued(employee_id):
    employee = Employee.objects.get(pk=employee_id)
    employee.clean_total_accrued()
