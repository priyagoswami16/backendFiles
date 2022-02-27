from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('photo', views.photo, name='photo'),
    path('present',views.present, name='present'),
    path('contact',views.contact, name='contact'),
]