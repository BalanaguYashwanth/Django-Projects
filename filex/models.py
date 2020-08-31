from django.db import models

import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.
class details(models.Model):
    person=models.CharField(max_length=150)
    place=models.CharField(max_length=250)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=150)
   

class orderdetails(models.Model):
    name=models.CharField(max_length=150)
    item=models.TextField()
    time=models.TextField()

class filesdata(models.Model):
    myname=models.CharField(max_length=150)
    myfile=models.ImageField(upload_to="photos/",default='/media/photos/default.jpg') 


class slidedata(models.Model):
    sname=models.CharField(max_length=150)
    sfile=models.ImageField(upload_to="photos/",default='/media/photos/default.jpg') 

