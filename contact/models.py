from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):

    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Contact(models.Model):

    frist_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50,blank=True)
    phone = models.CharField(max_length=14,blank=True)
    email = models.EmailField(max_length=250,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    descrition = models.TextField(max_length=500,blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True,upload_to='pictures/%Y/%m/%d')
    id_caregory = models.ForeignKey(Category,
                                    on_delete=models.SET_NULL,
                                    blank=True, 
                                    null=True)
    
    def __str__(self) -> str:
        return f'{self.frist_name}  {self.last_name}'
    
