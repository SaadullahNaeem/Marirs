from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/Employee/create/$', views.EmployeeCreate.as_view(), name='employee_create'),
    url(r'^api/Employee/list/$', views.EmployeeList.as_view(), name='employee_list'),
    url(r'^api/Employee/(?P<pk>\d+)/detail/$', views.EmployeeDetail.as_view(), name='employee_detail'),


    url(r'^api/addDepartment/$', views.DepartmentAdd.as_view(), name='add_department'),
    url(r'^api/deptartments/all/$', views.EmplyoeDeptGet.as_view(), name='all_department'),

    url(r'^api/Employee/addgroup/$', views.EmployeeGroupAdd.as_view(), name='add_Employee_group'),
    url(r'^api/Employee/group/all/$', views.EmplyoeGroupGet.as_view(), name='all_Employee_group'),
]

