from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User,auth,Group
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import permissions

# Create your views here.

class componentViewset(viewsets.ModelViewSet):
    serializer_class=componentSerializer
    queryset=component.objects.all()

class componentupdateViewset(viewsets.ModelViewSet):
    serializer_class=componentupdateSerializer
    queryset=componentupdate.objects.all()


class Iscustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='customer'):
            return False
        return True


class componentEachViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, Iscustomer,)

    serializer_class=componentEachSerializer
    queryset=componentEach.objects.all()

    
    # def check_permissions(self, request):

    #     for permission in self.get_permissions():
    #         if not permission.has_permission(request, self):
    #             self.permission_denied(
    #                 request, message=getattr(permission, 'message', None)
    #             )


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
            group=Group.objects.get(name='customer')
            mdata.groups.add(group)
            data['email']=mdata.email
            data['username']=mdata.username
            data['response']="successfully registered"
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        model=User.objects.all()
        serializer=registerSerializer(model,many=True)
        return Response(serializer.data)



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

class logoutView(APIView):

    def get(self,request):
        request.user.auth_token.delete()
        auth.logout(request)
        return Response("sucessfully logout")







    

