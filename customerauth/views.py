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


class customeruserprofileview(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def get(self,request):
        model=cutomeruserprofile.objects.get(customer_id=request.user.id)
        id=model.id
        model=cutomeruserprofile.objects.filter(id=id)
        serializer=customerprofileSerializer(model,many=True)
        return Response(serializer.data)



    def post(self,request):
        serializer=customerprofileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("error")
        

class registercutomerdata(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self,request):
        model=User.objects.get(username=request.user.username)
        serializer=customerRegisterSerializer(model)
        return Response(serializer.data)


class customerregisterView(APIView):

    def post(self,request):
        serializer=customerRegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid(raise_exception=True):
            cname=serializer.save()
            data['response']="successfully registered"
            data['username']=cname.username
            data['email']=cname.email
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class customerloginView(APIView):

    def post(self,request):
        serializers=customerLoginSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            user=serializers.save()
            auth.login(request,user)
            token,created=Token.objects.get_or_create(user=user)
            return Response({'token':token.key},status=200)
        return Response('unable to login retry once')



class customerlogout(APIView):

    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return Response("successfully logout")








