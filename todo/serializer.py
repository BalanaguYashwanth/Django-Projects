from rest_framework import serializers
from django.db import models
from rest_framework import exceptions
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate,login 
from .models import *

class todo_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model=todo_data
        fields='__all__'





    


