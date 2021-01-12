from decimal import Decimal

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

class Employee(MPTTModel):
    second_name = models.CharField(_('second name'), max_length=150)
    first_name = models.CharField(_('first name'), max_length=150)
    patronim = models.CharField(_('patronim'), max_length=150, blank=True)
    position = models.ForeignKey(
        'Position',
        on_delete=models.CASCADE,
        verbose_name=_('position'))
    employment_date = models.DateField(_('employment date'), auto_now=True)
    salary = models.DecimalField(
        _('salary'),
        decimal_places=2,
        max_digits=7,
        default=Decimal(0))
    total_accrued = models.DecimalField(
        _('total accrued'),
        decimal_places=2,
        max_digits=10,
        default=Decimal(0),
        help_text=_('Amount of all accrued salary since start of recording'))
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name=_('children'))

    class Meta:
        ordering = ['tree_id', 'lft']
        verbose_name = _('Employee')
        verbose_name_plural = _('Staff')

    class MPTTMeta:
        order_insertion_by = ('second_name', 'first_name')


class Position(models.Model):
    name = models.CharField(_('name'), max_length=150, blank=True)

    class Meta:
        verbose_name = _('Position')
        verbose_name_plural = _('Positions')

