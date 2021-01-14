from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from ..models import Employee
from .serializers import EmployeeSerializer
from .permissions import CanViewAPIPermission

class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated & CanViewAPIPermission]    
    queryset = Employee.objects.select_related('position', 'parent')
    serializer_class = EmployeeSerializer
    filterset_fields = ('level', )

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def self_employee_view(request):
    try:
        employee = Employee.objects.get(user=request.user)
    except Employee.DoesNotExist:
        raise NotFound
    return Response(EmployeeSerializer(employee, context={'request': request}).data)

