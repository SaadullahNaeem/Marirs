# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from CustomUser.models import User

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100, blank=False)

class EmployeeGroup(models.Model):
    name = models.CharField(max_length=100, blank=True)

class Employee(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    joining_date = models.DateField(blank=False)
    Termination_date = models.DateField(blank=True)
    status = models.CharField(max_length=100, blank=False)
    present_address = models.TextField(max_length=300, blank=False)
    permanent_address = models.TextField(max_length=300, blank=False)
    blood_group = models.CharField(max_length=30, blank=False)
    home_phone = models.IntegerField(max_length=13, blank=False)
    Cell_phone = models.IntegerField(max_length=13, blank=False)
    emergency_contact_person = models.CharField(max_length=100, blank=False)
    emergency_contact_number = models.IntegerField(max_length=100, blank=False)
    passport_no = models.IntegerField(max_length=100, blank=False)
    driving_license_no = models.IntegerField(max_length=100, blank=False)
    emp_package = models.CharField(max_length=100, blank=False)
    base_salary = models.IntegerField(blank=False)
    variable_salary = models.IntegerField(blank=True)
    provide_accommodation = models.BooleanField(default=False)
    provide_trans = models.BooleanField(default=False)
    emp_type = models.CharField(max_length=100, blank=False)
    emp_dept = models.CharField(max_length=100, blank=False)
    emp_designation = models.CharField(max_length=100, blank=False)
    emp_manager_name = models.CharField(max_length=100, blank=False)
    emp_group_fk = models.ForeignKey(EmployeeGroup,on_delete=models.CASCADE,blank=True,null=True)
    dept_fk = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)




