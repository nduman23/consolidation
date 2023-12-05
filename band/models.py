from django.db import models
#Add this
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255,blank=True,null=True,default=None)
    image = models.ImageField(upload_to='images/')

    