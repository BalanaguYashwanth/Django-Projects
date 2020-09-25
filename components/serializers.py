from rest_framework import serializers
from rest_framework import exceptions
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate
from .models import *

class componentSerializer(serializers.ModelSerializer):
    class Meta:
        model=component
        fields='__all__'

class componentupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=componentupdate
        fields='__all__'

class componentEachSerializer(serializers.ModelSerializer):
    class Meta:
        model=componentEach
        fields="__all__"

class customerdataSerializer(serializers.ModelSerializer):
    class Meta:
        model=customerdata
        fields='__all__'


class registerSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(max_length=150)
    last_name=serializers.CharField(max_length=150)
    password=serializers.CharField(max_length=150,write_only=True)
    username=serializers.CharField(max_length=150)
    email=serializers.EmailField(max_length=255,min_length=4)
    class Meta:
        model=User
        fields='__all__'

    def save(self):
        email=self.validated_data['email']
        username=self.validated_data['username']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':'email is already exists'})
        elif User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':'username is already exists'})
        else:
            user=User.objects.create(
                username=self.validated_data['username'],
                email=self.validated_data['email'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
                )
            password=self.validated_data['password']
            user.is_active=False
            user.set_password(password)
            user.save()
            return user

class loginSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=150)
    password=serializers.CharField(max_length=150)

    class Meta:
        model=User
        fields='__all__'
    
    def save(self):
        username=self.validated_data['username']
        password=self.validated_data['password']

        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                return user
            else:
                raise serializers.ValidationError({'user':'user is not a valid'})
        else:
            raise serializers.ValidationError({'error':'username and password must not be blank'})
        return user
      

