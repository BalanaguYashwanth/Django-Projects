from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField
from django.core.validators import RegexValidator

# Create your models here.
class details(models.Model):
    user=models.CharField(max_length=150)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phonenumber = models.CharField(validators=[phone_regex], max_length=10, blank=True) # validators should be a list