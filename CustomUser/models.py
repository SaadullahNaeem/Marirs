from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin,AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

# from .managers import UserManager

class User(AbstractUser):
    choices = (('hr','HR'),
               ('sales', 'Sales'),
               ('marketing', 'Marketing'),
               ('superusers', 'Superusers'),
               ('administrators', 'Administrators'),
               ('engineering',   'Engineering'),
               ('finance', 'Finance'),
               ('it', 'IT'),
               )
    state = models.CharField(max_length=40,choices=choices,default='')

    REQUIRED_FIELDS = ['email']


