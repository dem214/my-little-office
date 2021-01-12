from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StaffConfig(AppConfig):
    name = 'my_little_office.apps.staff'
    verbose_name = _('staff')

