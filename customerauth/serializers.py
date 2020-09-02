from rest_framework import serializers,exceptions
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from .models import *

class customerprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model=cutomeruserprofile
        fields="__all__"

class customerrequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=customerrequest
        fields='__all__'



class customerRegisterSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(max_length=150)
    last_name=serializers.CharField(max_length=150)
    username=serializers.CharField(max_length=150)
    password=serializers.CharField(max_length=150,write_only=True)
    email=serializers.EmailField(max_length=255)

    class Meta:
        model=User
        fields='__all__'

    def save(self):
        email=self.validated_data['email']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':'emailid is already exists'})
        else:
            user=User.objects.create(
                username=self.validated_data['username'],
                email=self.validated_data['email'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name']
            )
            password=self.validated_data['password']
            user.is_active=True
            user.set_password(password)
            user.save()
            return user

class customerLoginSerializer(serializers.ModelSerializer):
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
                if user.is_active:
                    return user
                else:
                    raise serializers.ValidationError({'user':'user is bot active'})
            else:
                raise serializers.ValidationError({'user':'user is not valid'})
        else:
            raise serializers.ValidationError({'error':'username and password must not be blank'})
        return user







