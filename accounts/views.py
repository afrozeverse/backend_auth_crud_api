from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class Registerview(APIView):
    def post(self,request):
        data=request.data
        serializer=RegisterSerializer(data=data)
        if serializer.is_valid():
            user=serializer.save()
            return Response({
                "message":"User created successfully.",
                "status":True,
                "data":serializer.data
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Loginview(APIView):
    def post(self,request):
        data=request.data
        username=data['username']
        password=data['password']
        user=User.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh=RefreshToken.for_user(user)
            return Response({
                "access_token":str(refresh.access_token),
                "refresh_token":str(refresh)
            })
        return Response({
            "message":"Invalid credentials"
        }, status=status.HTTP_400_BAD_REQUEST)