from rest_framework import viewsets,routers,serializers
from .models import *
from .serializers import *
from rest_framework.parsers import FormParser,MultiPartParser,JSONParser
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status



class pgdataViewsets(viewsets.ModelViewSet):
    queryset=pgdata.objects.all()
    serializer_class=pgdataSerializer


class customerdataViewsets(viewsets.ModelViewSet):
    queryset=customerdata.objects.all()
    serializer_class=customerdataSerializer
    


class filedataViewsets(viewsets.ModelViewSet):
   
    queryset=filedata.objects.all()
    serializer_class=filedataSerializer


class memberdataViewsets(viewsets.ModelViewSet):
    queryset=memberdata.objects.all()
    serializer_class=memberdataSerializer




    

