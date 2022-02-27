from xml.etree.ElementInclude import include
from django.shortcuts import render

# Create your views here.
from django.contrib import admin
from django.urls import path

def home(request):
    return render(request, 'index.html')

def details(request):
    return render(request, 'details.html')