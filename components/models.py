from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.

class component(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    component_name=models.CharField(max_length=150)
    title=models.CharField(max_length=150)
    description=models.TextField()
    timestamp=models.DateField(auto_now_add=True)
    reference_id=models.CharField(max_length=250)
    percentage=models.IntegerField(null=True,blank=True)


class componentEach(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    cname=models.CharField(max_length=150)

    
class customerdata(models.Model):
    user_name=models.CharField(max_length=150)
    reference_number=models.CharField(max_length=100,unique=True)
