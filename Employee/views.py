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
from .serelizers import *

from django.shortcuts import render

# Create your views here.
class EmployeeCreate(FormView):
    form_class = EmployeeCreationForm
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(EmployeeCreate, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        get_data = request.POST
        form = EmployeeCreationForm(request.POST or None)
        if form.is_valid():
            if Employee.objects.filter(email__exact=get_data['email']).exists():
                return Response({'errors': {'__all__': ['Email Already Exist']}},
                             status=status.HTTP_200_OK)
            else:
                form.save()
                deptfk = get_data['dept_fk']
                EG = get_data['emp_group']
                userid = request.user.id
                empobj = Employee.objects.get(id = get_data['id'])
                empobj.dept_fk_id = deptfk
                empobj.user_id = userid
                empobj.emp_group_fk_id = EG
                empobj.save()

                fname = get_data['first_name']
                lname = get_data['last_name']
                makepass = str(fname)+str(lname)
                user = User.objects.create(first_name=get_data['first_name'],
                                       username=str(get_data['first_name'])+str(get_data['last_name']),
                                       last_name=get_data['last_name'],
                                       email=get_data['email'],
                                       password=make_password(makepass),
                                       state=get_data['emp_group'],
                                       )
                user.save()
                return Response({'result': 'success'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'result': 'error'},
                            status=status.HTTP_200_OK)


class EmployeeList(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeDetail(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter(id=self.kwargs['pk'])


class DepartmentAdd(FormView):
    form_class = AddDepartmentForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DepartmentAdd, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = AddDepartmentForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            return Response({'result': 'Form is not valid'},
                            status=status.HTTP_200_OK)


class EmployeeGroupAdd(FormView):
    form_class = AddEmployeeForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(EmployeeGroupAdd, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            return Response({'result': 'Form is not valid'},
                            status=status.HTTP_200_OK)


class EmplyoeGroupGet(generics.ListAPIView):
    serializer_class = EmployeeGroupGetSerializer

    def get_queryset(self):
         return EmployeeGroup.objects.exclude(name__contains='HR')


class EmplyoeDeptGet(generics.ListAPIView):
    serializer_class = DepartmentGetSerializer

    def get_queryset(self):
        return Department.objects.all()