from decimal import Decimal

from django.contrib import admin
from .models import Employee, Position

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    fields = (
        'second_name',
        'first_name',
        'patronim',
        'position'
        'salary',
        'total_accrued'
    )

    list_filters = ('position', 'level')

    actions = ('clear_total_accrued')

    def clear_total_accrued(self, request, queryset):
        queryset.update(total_accrued=Decimal(0))

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass
