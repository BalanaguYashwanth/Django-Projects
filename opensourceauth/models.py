from django.db import models
from django.contrib.auth.models import User,auth
# Create your models here.

class userprofile(models.Model):
    owner_id=models.OneToOneField(User,on_delete=models.CASCADE)
    start_point=models.CharField(max_length=255)
    end_point=models.CharField(max_length=255)
    license_number=models.PositiveIntegerField()
    registration_number=models.PositiveIntegerField()
    service_days=models.SmallIntegerField()
    age=models.SmallIntegerField()
    shift=models.CharField(max_length=100)
    charge_per_trip=models.SmallIntegerField()
    category=models.CharField(max_length=100)
    aadhar_number=models.PositiveIntegerField()
    





