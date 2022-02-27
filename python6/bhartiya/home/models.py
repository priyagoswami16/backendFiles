from django.db import models

# Create your models here.

class test(models.Model):
    fname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, null=True)