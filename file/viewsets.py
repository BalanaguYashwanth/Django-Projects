from rest_framework import viewsets
from .serializers import *
from .models import *

class detailsViewsets(viewsets.ModelViewSet):
    queryset=details.objects.all()
    serializer_class=detailsSerializer

   