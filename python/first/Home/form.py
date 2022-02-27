from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import student 
from .models import register,contact , products



class registerform(forms.ModelForm):
    class Meta:
       model = register
       fields = '__all__'
class productsform(forms.ModelForm):
    class Meta:
       model = products
       fields = '__all__'

class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'