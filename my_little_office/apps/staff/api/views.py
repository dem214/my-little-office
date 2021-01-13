from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Employee
from .serializers import EmployeeSerializer
from .permissions import CanViewAPIPermission

class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated & CanViewAPIPermission]    
    queryset = Employee.objects.select_related('position', 'parent')
    serializer_class = EmployeeSerializer
    filterset_fields = ('level', )
