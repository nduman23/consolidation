from django.db import models
#Add this
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Band(models.Model):
    """
    Represents a musical band.

    Attributes:
        name (models.CharField): The name of the band. Max length is 100 characters.
        description (models.TextField): A brief description of the band. This field is optional.
            Max length is 255 characters. Can be blank, null, or set to a default value.
        image (models.ImageField): An image representing the band. The image is stored in the
            'images/' directory.
    """

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255,blank=True,null=True,default=None)
    image = models.ImageField(upload_to='images/')

    