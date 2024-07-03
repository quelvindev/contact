from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):

    fist_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50,blank=True)
    phone = models.CharField(max_length=14)
    email = models.EmailField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    descrition = models.TextField(max_length=500)
    ...
