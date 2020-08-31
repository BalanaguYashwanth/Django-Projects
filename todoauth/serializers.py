from .models import *
from rest_framework import serializers
from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=65, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    class Meta:
        model=User
        fields='__all__'    

    # def validate(self,data):
    #     email=data.get("email",""),
    #     password=make_password(data.get("password")),
        
        
        
    #     if User.objects.filter(email=email).exists():
    #         raise exceptions.ValidationError("email is exists")
    #     return super().validate(data)

    # def create(self,validated_data):
    #     return User.objects.create(**validated_data)

    def save(self):
        email=self.validated_data['email']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email-id" : "email is already exists"})
        else:    
            user = User.objects.create(
                email=self.validated_data['email'],
                username=self.validated_data['username'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
                ) 
            password=self.validated_data['password']
            user.is_active = False
            user.set_password(password)
            user.save()
            return user


class loginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=150)
    password=serializers.CharField(max_length=150)


    def validate(self,data):
        username=data.get("username","")
        password=data.get("password","")
        
        if username and password:
            user=auth.authenticate(username=username,password=password)
            if user:
                    data['user']=user
            else:
                raise exceptions.ValidationError("user is not valid")
        else:
            raise exceptions.ValidationError("username and password not to be blank")
        return data
    

class logoutSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=150)
    password=serializers.CharField(max_length=150)

    def validate(self,data):
        username=data.get("username","")
        password=data.get("password","")
        
        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data['user']=user
                else:
                    raise exceptions.ValidationError("user is exists")
            else:
                raise exceptions.ValidationError("user is not valid")
        else:
            raise exceptions.ValidationError("username and password not to be blank")
        return data






















