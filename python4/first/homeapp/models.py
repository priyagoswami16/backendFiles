from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=30, null=True)
    massage = models.TextField(max_length=200, null=True)
