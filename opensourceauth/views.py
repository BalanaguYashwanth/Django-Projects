from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User,auth
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
from rest_framework import status
from .serializers import *
from .models import *
# Create your views here.

class userprofileView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self,request):
        model=User.objects.filter(id=request.user.id)
        serializer=registerSerializer(model,many=True)
        return Response(serializer.data)


    def putd(self,request):
        model=userprofile.objects.get(owner_id=request.user.id)
        id=model.id
        model=userprofile.objects.filter(id=id)
        serializer=userprofileSerializer(model,many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer=userprofileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("error")

class allprofiles(APIView):
    
    def get(self,request):
        model=userprofile.objects.all()
        serializer=userprofileSerializer(model,many=True)
        return Response(serializer.data)


class mainuserprofile(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def get(self,request):
        model=userprofile.objects.get(owner_id=request.user.id)
        id=model.id
        model=userprofile.objects.filter(id=id)
        serializer=userprofileSerializer(model,many=True)
        return Response(serializer.data)




class userprofileView_one(APIView):
    
    def delete(self,request,id):
        model=userprofile.objects.get(id=id)
        model.delete()
        return Response("successfully deleted")


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


class logout(APIView):

    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return Response("successfully logout")






