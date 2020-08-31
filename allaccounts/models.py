from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class allprofiles(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    pg_id=models.IntegerField()

    

