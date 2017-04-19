from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('FrontEnd.urls')),
url(r'^', include('CustomUser.urls')),
url(r'^', include('Employee.urls')),

]
