# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):

    choices = (('Active','Active'),('Terminated','Terminated'))
    blood_choices = (('A+','A+'),('B+','B+'),('A-','A-'),('B-','B-'),('AB+','AB+'),('AB-','AB-'),('C+','C+'),('C-','C-'),)
    emptype = (('Fulltime','Fulltime'),('Contractor','Contractor'))
    # dept = (('hr','HR'),('ser','Services'),('Mana','Management'),('payroll','Payroll'),)
    groups_emp = (
               ('sales', 'Sales'),
               ('marketing', 'Marketing'),
               ('administrators', 'Administrators'),
               ('engineering', 'Engineering'),
               ('finance', 'Finance'),
               ('it', 'IT'),
               )

    first_name = models.CharField(max_length=100,blank=False)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    joining_date = models.DateField( blank=True)
    Joined_date = models.DateField( blank=True)
    Termination_date = models.DateField( blank=False)
    status = models.CharField(max_length=100,choices=choices, blank=False)
    present_address = models.TextField(max_length=300, blank=False)
    permanent_address = models.BooleanField(default=False)
    blood_group= models.CharField(max_length=30,choices=blood_choices, blank=False)
    home_phone =models.IntegerField(blank=True)
    Cell_phone =models.CharField(max_length=100, blank=True)
    emergency_contact_person=models.CharField(max_length=100, blank=False)
    emergency_contact_number=models.CharField(max_length=100, blank=False)
    passport_no =models.CharField(max_length=100, blank=False)
    driving_license_no = models.IntegerField(blank=False)
    emp_package = models.CharField(max_length=100, blank=True)
    base_salary = models.IntegerField(blank=True)
    variable_salary = models.IntegerField(blank=True)
    provide_accommodation = models.BooleanField(default=False)
    provide_trans = models.BooleanField(default=False)
    emp_type = models.CharField(max_length=100,choices=emptype, blank=True)
    emp_dept = models.CharField(max_length=100, blank=True) #dropdown
    emp_designation = models.CharField(max_length=100, blank=True)  #dropdown
    emp_manager_name = models.CharField(max_length=100, blank=True) #dropdown
    emp_group = models.CharField(max_length=100,choices=groups_emp, blank=True)



