from django.db import models

# Create your models here.
class todo_data(models.Model):
    name=models.CharField(max_length=150)

    