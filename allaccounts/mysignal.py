from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from allaccounts.models import *


@receiver(post_save,sender=User)
def save_data(sender,instance,created,**kwargs):
    if created:
        allprofiles.objects.create(user=instance)
    else:
        instance.allprofiles.save()



