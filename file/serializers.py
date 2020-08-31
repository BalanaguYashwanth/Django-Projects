from rest_framework import routers,serializers,viewsets
from .models import *

class detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=details
        fields='__all__'
