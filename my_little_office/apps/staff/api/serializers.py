from rest_framework import serializers

from ..models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'second_name',
            'first_name',
            'position__name'
            'patronim',
            'salary',
            'total_accrued')