from rest_framework import serializers,routers
from .models import *
from django.contrib.contenttypes.models import ContentType


class pgdataSerializer(serializers.ModelSerializer):
    class Meta:
        model=pgdata
        fields='__all__'

class customerdataSerializer(serializers.ModelSerializer):
    class Meta:
        model=customerdata
        fields='__all__'

class filedataSerializer(serializers.ModelSerializer):
    class Meta:
        model=filedata
        fields='__all__'


class memberdataSerializer(serializers.ModelSerializer):
    class Meta:
        model=memberdata
        fields='__all__'


        