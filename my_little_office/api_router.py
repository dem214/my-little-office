from rest_framework.routers import DefaultRouter

from .apps.staff.api.views import EmployeeViewSet

router = DefaultRouter()
router.register('staff', EmployeeViewSet)