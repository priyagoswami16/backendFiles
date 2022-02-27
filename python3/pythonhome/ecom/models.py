from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    details = models.CharField(max_length=200, null=True)
    kuch_bhi = models.CharField(max_length=200, null=True)