from email import message
from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20, null=True)
    course = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=10, null=True)
    message = models.TextField(max_length=500, null=True)

class products(models.Model):
    name = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=20, null=True)
    img = models.FileField(upload_to= "static")
   
    def __str__(self):
        return self.name