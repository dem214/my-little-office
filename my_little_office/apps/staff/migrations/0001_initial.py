# Generated by Django 3.1.5 on 2021-01-12 20:12

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_name', models.CharField(max_length=150, verbose_name='second name')),
                ('first_name', models.CharField(max_length=150, verbose_name='first name')),
                ('patronim', models.CharField(blank=True, max_length=150, verbose_name='patronim')),
                ('employment_date', models.DateField(auto_now=True, verbose_name='employment date')),
                ('salary', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=7, verbose_name='salary')),
                ('total_accrued', models.DecimalField(decimal_places=2, default=Decimal('0'), help_text='Amount of all accrued salary since start of recording', max_digits=10, verbose_name='total accrued')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('chief', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subordinate', to='staff.employee', verbose_name='chief')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.position', verbose_name='position')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Staff',
                'ordering': ['tree_id', 'lft'],
            },
        ),
    ]