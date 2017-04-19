# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import FormView, BaseDetailView,View

from .models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# Create your views here.
class SigninView(APIView):


    def post(self, request):
        data = request.data
        if not data.has_key('username') or not data.has_key('password'):
            return Response({'errors': {'__all__': ['Email and Password are required']}},
                            status=status.HTTP_200_OK)

        check_user = User.objects.filter(email__iexact=data['username'])
        if check_user.exists():
            user = check_user.first()
            password = data['password']

            if user is not None and user.check_password(password):
                payload = jwt_payload_handler(user)
                access_token = jwt_encode_handler(payload)

                return Response({'result': 'success', 'user_name': user.first_name.title(), 'access_token': access_token, 'email': user.email, 'user_id': user.id},
                                status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'__all__': ['Email and Password are not matched']}},
                                status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'__all__': ['Email and Password are not matched']}},
                            status=status.HTTP_200_OK)


