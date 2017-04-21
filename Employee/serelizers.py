from rest_framework import serializers
from .models import *
class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeGroupGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeGroup
        fields = '__all__'


class DepartmentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'