from dataclasses import fields
from .models import Contacts
from django import forms
from django.forms import ModelForm



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
       