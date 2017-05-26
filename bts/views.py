from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView


from bts.serializers import AuthParamsSerializer


class LoginView(APIView):
    permission_classes =[]

    def post(self, request):
        serializer = AuthParamsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = auth.authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to dashboard
            return HttpResponse('You are successfully login')
        else:
            err_msg = 'Please enter your username and password below.'
            return HttpResponse(err_msg)

    def logout(self, request):
        auth.logout(request)
        return HttpResponse('You are successfully logout')
