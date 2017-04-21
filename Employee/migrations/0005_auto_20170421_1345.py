# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 13:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0004_auto_20170421_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dept_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Employee.Department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_group_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Employee.EmployeeGroup'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
