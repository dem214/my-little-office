from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .apps.staff.api.views import EmployeeViewSet, self_employee_view

router = DefaultRouter()
router.register('staff', EmployeeViewSet)

urlpatterns = router.urls + [
    path('self/', self_employee_view, name='self_view'),
    path('token/', obtain_auth_token)
]
