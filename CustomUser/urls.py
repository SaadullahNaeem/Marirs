from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^accounts/signin/$', views.SigninView.as_view(), name='Login')
]

