# Generated by Django 3.1.5 on 2021-01-12 20:17

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='chief',
        ),
        migrations.AddField(
            model_name='employee',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrem', to='staff.employee', verbose_name='chief'),
        ),
    ]
