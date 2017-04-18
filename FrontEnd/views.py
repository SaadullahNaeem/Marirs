# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def landing_page(request):
    return render(request, 'FrontEnd/landing_page.html', {})
