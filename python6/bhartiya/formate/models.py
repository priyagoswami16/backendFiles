
from django.db import models

# Create your models here.
class resform(models.Model):
    First_Name = models.CharField(max_length=20, null=True)
    Last_Name = models.CharField(max_length=20, null=True)
    # father_name = models.CharField(max_length=20, null=True)
    # mother_name = models.CharField(max_length=20, null=True)
    # DOB = models.DateField(unique=date)
    # email = models.CharField(max_length=20, null=True)
    # address = models.TextField(max_length=200, null=True)
    # pin_code = models.CharField(max_length=10, null=True)
    # mobile = models.CharField(max_length=20, null=True)
    # gender = models.CharField(max_length=10, null=True)
    # state = models.CharField(max_length=20, null=True)
    # city = models.CharField(max_length=20, null=True)
    # date = models.DateField(default= date.today)


# class test(models.Model):
#     fname = models.CharField(max_length=20, null=True)
#     lname = models.CharField(max_length=20, null=True)