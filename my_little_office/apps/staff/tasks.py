from my_little_office.celery import app
from .models import Employee


@app.task(bind=True)
def clean_total_accrued(self, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    employee.clean_total_accrued()
