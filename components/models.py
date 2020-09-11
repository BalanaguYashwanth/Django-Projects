from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.

class component(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    component_name=models.CharField(max_length=150)
    title=models.CharField(max_length=150)
    description=models.TextField()
    timestamp=models.DateField(auto_now_add=True)


class componentEach(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=150)

    

