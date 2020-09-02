from django.db import models
from django.contrib.auth.models import User,auth
# Create your models here.
class cutomeruserprofile(models.Model):
    customer_id=models.OneToOneField(User,on_delete=models.CASCADE)
    customer_gender=models.CharField(max_length=150)
    customer_phonenumber=models.BigIntegerField(unique=True) 
    age=models.SmallIntegerField()
    customer_name=models.CharField(max_length=150)
    
class customerrequest(models.Model):
    name=models.CharField(max_length=150)
    phonenumber=models.BigIntegerField()
    startpoint=models.CharField(max_length=150)
    endpoint=models.CharField(max_length=150)
    expectedtime=models.CharField(max_length=150)
    requestshift=models.CharField(max_length=150)
    requestcategory=models.CharField(max_length=250)
