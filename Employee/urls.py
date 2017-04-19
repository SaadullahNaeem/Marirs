from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^Employee/create/$', views.EmployeeCreate.as_view(), name='employee_create'),
    url(r'^Employee/list/$', views.EmployeeList.as_view(), name='employee_list'),
    url(r'^Employee/(?P<pk>\d+)/detail/$', views.EmployeeDetail.as_view(), name='employee_detail')
]

