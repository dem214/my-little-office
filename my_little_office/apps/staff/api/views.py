from rest_framework import viewsets

from ..models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = Employee.objects.select_related('position', 'parent')
    serializer_class = EmployeeSerializer
    filterset_fields = ('level', )
