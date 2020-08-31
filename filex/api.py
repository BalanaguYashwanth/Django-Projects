from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import action, parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser,FileUploadParser,FormParser
from rest_framework.response import Response
#from rest_framework_csv.parsers import CSVParser
#from posts.models import Post
#from posts.serializers import PostSerializer     
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required


#from filex.utils import MultipartJsonParser

class detailed(APIView):
    

    def get(self,request):
        model=details.objects.all()
        serializer=detailsSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=detailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request):
        model=details.objects.all()
        model.delete()
        return Response("Successfully deleted all the datas")

class orderdetailed(APIView):
    
    def get(self,request):
        model=orderdetails.objects.all()
        serializer=orderdetailsSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=orderdetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request):
        model=orderdetails.objects.all()
        model.delete()
        return Response("Successfully deleted all the datas")

class filesdatadetailed(APIView):

    def get(self,request):
        model=filesdata.objects.all()
        serializer=filesdataSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=filesdataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


    def delete(self,request):
        model=filesdata.objects.all()
        model.delete()
        return Response("Successfully deleted all the datas")

class slidedatadetailed(APIView):

    def get(self,request):
        model=slidedata.objects.all()
        serializer=slidedataSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=slidedataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


    def delete(self,request):
        model=slidedata.objects.all()
        model.delete()
        return Response("Successfully deleted all the datas")


class Moredetail(APIView):

    def get(self,request,id):
        model=details.objects.get(id=id)
        serializer=detailsSerializer(model)
        return Response(serializer.data)
    
    def put(self,request,id):
        model=details.objects.get(id=id)
        serializer=detailsSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    
    def delete(self,request,id):
        model=details.objects.get(id=id)
        model.delete()
        return Response("Successful deleted the data")

class orderMoredetail(APIView):

    def get(self,request,id):
        model=orderdetails.objects.get(id=id)
        serializer=orderdetailsSerializer(model)
        return Response(serializer.data)
    
    def put(self,request,id):
        model=orderdetails.objects.get(id=id)
        serializer=orderdetailsSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    
    def delete(self,request,id):
        model=orderdetails.objects.get(id=id)
        model.delete()
        return Response("Successful deleted the data")


class filesdataMoredetail(APIView):

    def get(self,request,id):
        model=filesdata.objects.get(id=id)
        serializer=filesdataSerializer(model)
        return Response(serializer.data)

    def put(self,request,id):
        model=filesdata.objects.get(id=id)
        serializer=filesdataSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    
    def delete(self,request,id):
        model=filesdata.objects.get(id=id)
        model.delete()
        return Response("Successful deleted the data")


class slidedataMoredetail(APIView):

    def get(self,request,id):
        model=slidedata.objects.get(id=id)
        serializer=slidedataSerializer(model)
        return Response(serializer.data)

    def put(self,request,id):
        model=slidedata.objects.get(id=id)
        serializer=slidedataSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    
    def delete(self,request,id):
        model=slidedata.objects.get(id=id)
        model.delete()
        return Response("Successful deleted the data")

        
