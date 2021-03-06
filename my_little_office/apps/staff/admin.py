from decimal import Decimal

from django.contrib import admin
from django.utils.translation import gettext as _
from django.utils.html import format_html
from django.urls import reverse

from .models import Employee, Position
from .tasks import clean_total_accrued


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    fields = (
        'second_name',
        'first_name',
        'patronym',
        'parent',
        'position',
        'employment_date',
        'salary',
        'total_accrued',
        'user'
    )
    list_display = ('full_name', 'chief_link',
                    'position', 'salary', 'total_accrued')
    list_filter = ('position', 'level')
    actions = ['clear_total_accrued']
    date_hierarchy = 'employment_date'

    def chief_link(self, obj):
        """Generate href to chief person."""
        if obj.parent:
            return format_html(
                '<a  href="{0}" >{1}</a>&nbsp;',
                reverse('admin:staff_employee_change', args={obj.parent.id}),
                str(obj.parent)
            )
    chief_link.allow_tags = True
    chief_link.short_description = _('chief')

    def clear_total_accrued(self, request, queryset):
        """Add action to clear field `total_accrued` at selected staff."""
        ASYNC_EDGE = 20
        if queryset.count() <= ASYNC_EDGE:
            queryset.update(total_accrued=Decimal(0))
        else:
            for e in queryset:
                clean_total_accrued(e.pk)
    clear_total_accrued.short_description = _('Clear field "total accrued"')

    def get_queryset(self, request):
        return super().get_queryset(request)\
            .prefetch_related('parent', 'position')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass
