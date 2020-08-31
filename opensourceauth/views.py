from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User,auth
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *
# Create your views here.

class userprofileView(APIView):

    def get(self,request):
        model=userprofile.objects.all()
        serializer=userprofileSerializer(model,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        model=userprofile.objects.all(data=request.data)
        serializer=userprofileSerializer(model)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("error")


class registers(APIView):
    
    def post(self,request):
        serializer=registerSerializer(data=request.data)
        data={}
        if serializer.is_valid(raise_exception=True):
            mname=serializer.save()
            data['response']="successfully registered"
            data['username']=mname.username
            data['email']=mname.email
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class logins(APIView):
    
    def post(self,request):
        serializer=loginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            auth.login(request,user)
            token,created=Token.objects.get_or_create(user=user)
            return Response({'token':token.key},status=200)
        return Response('unable to login retry once')


            






