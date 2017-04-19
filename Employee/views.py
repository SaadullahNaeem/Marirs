# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from Employee.serelizers import EmployeeSerializer
from .forms import *
from .models import *
from CustomUser.models import User

from django.shortcuts import render

# Create your views here.
class EmployeeCreate(FormView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(EmployeeCreate, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        get_data = request.POST

        if Employee.objects.filter(email__exact=get_data['email']).exists():
                return Response({'errors': {'__all__': ['Email Already Exist']}},
                             status=status.HTTP_200_OK)
        else:
                get_obj = Employee.objects.create(
                first_name=get_data['first_name'],
                last_name=get_data['last_name'],
                middle_name = get_data['middle_name'],
                joining_date=get_data['joining_date'],
                email=get_data['email'],
                status=get_data['status'],
                Termination_date=get_data['Termination_date'],
                present_address=get_data['present_address'],
                permanent_address=get_data['permanent_address'],
                blood_group=get_data['blood_group'],
                home_phone=get_data['home_phone'],
                Cell_phone=get_data['Cell_phone'],
                emergency_contact_person=get_data['emergency_contact_person'],
                emergency_contact_number=get_data['emergency_contact_number'],
                passport_no=get_data['passport_no'],
                driving_license_no=get_data['driving_license_no'],
                emp_package=get_data['emp_package'],
                base_salary=get_data['base_salary'],
                variable_salary=get_data['variable_salary'],
                provide_accommodation=get_data['provide_accommodation'],
                provide_trans=get_data['provide_trans'],
                emp_type=get_data['emp_type'],
                emp_dept=get_data['emp_dept'],
                emp_designation=get_data['emp_designation'],
                emp_manager_name=get_data['emp_manager_name'],
                emp_group=get_data['emp_group'],

                )
                get_obj.save()
                fname = get_data['first_name']
                lname = get_data['last_name']
                makepass = str(fname)+str(lname)
                user = User.objects.create(first_name=get_data['first_name'],
                                       last_name=get_data['last_name'],
                                       email=get_data['email'],
                                       password=make_password(makepass),
                                       state=get_data['emp_group'],
                                       )
                user.save()
                return Response({'result': 'success'},
                            status=status.HTTP_200_OK)



class EmployeeList(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeDetail(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_object(self):
        return Employee.objects.get(id=self.kwargs['pk'])
