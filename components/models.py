from django.db import models
from django.contrib.auth.models import User,auth
from io import BytesIO
from PIL import Image
from django.core.files import File

# Create your models here.

def user_directory_path(instance,filename):
    return 'posts/{0}/{1}'.format(instance.id,filename)

def compress(image):
        im = Image.open(image)
        # create a BytesIO object
        im_io = BytesIO() 
        # save image to BytesIO object
        im.save(im_io, 'JPEG', quality=70) 
        # create a django-friendly Files object
        new_image = File(im_io, name=image.name)
        return new_image

class component(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    component_name=models.CharField(max_length=150)
    title=models.CharField(max_length=150)
    description=models.TextField()
    timestamp=models.DateField(auto_now_add=True)
    reference_id=models.CharField(max_length=250)
    percentage=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to=user_directory_path)

    

    def save(self, *args, **kwargs):
            if self.image:
                if self.image.size > (300 * 1024):
                    # call the compress function
                    new_image = compress(self.image)
                    # set self.image to new_image
                    self.image = new_image
                    # save
            super().save(*args, **kwargs)



class componentEach(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    cname=models.CharField(max_length=150)


class customerdata(models.Model):
    user_name=models.CharField(max_length=150)
    reference_number=models.CharField(max_length=100,unique=True)
