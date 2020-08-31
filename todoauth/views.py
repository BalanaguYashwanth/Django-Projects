from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.contrib.auth import login,logout
from django.contrib.auth.models import User,auth
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication,BasicAuthentication
# Create your views here.

#@api_view
# class retriveTokenView(APIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticatedOrReadOnly,)


@api_view(['GET',])
@permission_classes((IsAuthenticated, ))    
def api_get( request):
    if request.user.is_authenticated:
        model=User.objects.get(username=request.user.username)
        serializer=ProfileSerializer(model)
        return Response(serializer.data)
    else:
        return Response("not")


class RegisterView(GenericAPIView):
    serializer_class=UserSerializer
   
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        data={}
        if serializer.is_valid(raise_exception=True):
            mname=serializer.save()
            data['response']="successfully registered"
            data['username']=mname.username
            data['first_name']=mname.email
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class loginView(APIView):

    def post(self,request):
        serializer=loginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.validated_data['user']
            login(request,user)
            token,created = Token.objects.get_or_create(user=user)
            return Response({"token":token.key},status=200)
        return Response("Unable to login retry once ")

# class loginView(APIView):
#     authentication_classes = (BasicAuthentication,SessionAuthentication)

#     def post(self, request, format=None):
#         data = request.data

#         username = data.get('username', None)
#         password = data.get('password', None)

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 token,created = Token.objects.get_or_create(user=user)
#                 return Response({"token":token.key},status=200)
#             else:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)



class logoutView(APIView):

    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return Response("successfully logged out ")
        
