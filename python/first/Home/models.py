from django.db import models


# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20 , null=True)
    email = models.CharField(max_length=30 , null=True)
    massage = models.TextField(max_length=500 , null=True)

class register(models.Model):
    pwd = models.CharField(max_length=10,null=True)
    name = models.CharField(max_length=20 , null=True)
    email = models.CharField(max_length=30 , null=True)
    massage = models.TextField(max_length=500 , null=True)

class contact(models.Model):
    pwd = models.CharField(max_length=10,null=True)
    name = models.CharField(max_length=20 , null=True)
    email = models.CharField(max_length=30 , null=True)
    massage = models.TextField(max_length=500 , null=True)
    mobile = models.CharField(max_length=500 , null=True)     

class products(models.Model):
    name = models.CharField(max_length=20 , null=True)
    price = models.CharField(max_length=30 , null=True)
    img = models.FileField(upload_to= "static")

    pass


    def __str__(self):
        return self.name
   
