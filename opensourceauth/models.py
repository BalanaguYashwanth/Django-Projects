from django.db import models
from django.contrib.auth.models import User,auth

class userprofile(models.Model):
    owner_id=models.OneToOneField(User,on_delete=models.CASCADE)
    start_point=models.CharField(max_length=255)
    end_point=models.CharField(max_length=255)
    license_number=models.PositiveIntegerField(unique = True)
    registration_number=models.PositiveIntegerField(unique = True)
    service_days=models.SmallIntegerField()
    age=models.SmallIntegerField()
    shift=models.CharField(max_length=100)
    charge_per_trip=models.SmallIntegerField()
    category=models.CharField(max_length=100)
    aadhar_number=models.PositiveIntegerField(unique = True)
    gender=models.CharField(max_length=100)
    username=models.CharField(max_length=150)


class userbookings(models.Model):
    driverid=models.SmallIntegerField()
    driver_name=models.CharField(max_length=150)
    booked_name=models.CharField(max_length=150)
    booked_phonenumber=models.BigIntegerField()
    startingpoint=models.CharField(max_length=255)
    endingpoint=models.CharField(max_length=255)
    charges=models.SmallIntegerField()







