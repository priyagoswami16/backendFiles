from dataclasses import fields
from django.forms import ModelForm
from django import forms  
from .models import student, products


class studentform(forms.ModelForm):  
    class Meta:
      model = student
      fields = '__all__'

class productsform(forms.ModelForm):  
    class Meta:
      model = products
      fields = '__all__'      