from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User,auth
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly

# Create your views here.

class componentViewset(viewsets.ModelViewSet):
    

    serializer_class=componentSerializer
    queryset=component.objects.all()

class componentEachViewset(viewsets.ModelViewSet):
    serializer_class=componentEachSerializer
    queryset=componentEach.objects.all()


class registerprofile(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        model=User.objects.filter(id=request.user.id)
        serializer=registerSerializer(model,many=True)
        return Response(serializer.data)



class registerView(APIView):
    
    def post(self,request):
        serializer=registerSerializer(data=request.data)
        data={}
        if serializer.is_valid(raise_exception=True):
            mdata=serializer.save()
            data['email']=mdata.email
            data['username']=mdata.username
            data['response']="successfully registered"
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class customerdataViewset(viewsets.ModelViewSet):
    serializer_class=customerdataSerializer
    queryset=customerdata.objects.all()


class loginView(APIView):

    def post(self,request):
        serializer=loginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            auth.login(request,user)
            token,created=Token.objects.get_or_create(user=user)
            return Response({'token':token.key},status=200)
        else:
            return Response('unable to login retry once')






    

