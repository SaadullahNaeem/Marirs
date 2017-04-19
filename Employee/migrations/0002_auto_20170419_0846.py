# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Joined_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='base_salary',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='driving_license_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_dept',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_designation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_manager_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_package',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_type',
            field=models.CharField(blank=True, choices=[('Fulltime', 'Fulltime'), ('Contractor', 'Contractor')], max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='home_phone',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='permanent_address',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='provide_accommodation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='provide_trans',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='variable_salary',
            field=models.IntegerField(blank=True),
        ),
    ]
