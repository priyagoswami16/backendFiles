from email import message
from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=20, null=True)
    img = models.FileField(upload_to='static')

class Contacts(models.Model):
    fname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=20, null=True)
    emailaddress = models.EmailField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    message = models.CharField(max_length=20, null=True)

class Categroy(models.Model):
    imgone = models.FileField(upload_to='static')

class Scrdile(models.Model):   
    imgtwo = models.FileField(upload_to='static')

class Cruasal(models.Model):
    imgthree = models.FileField(upload_to='static')

 
  


    
    
    