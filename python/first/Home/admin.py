from django.contrib import admin
from .models import student,register,contact,products

# Register your models here.
admin.site.register(student)
admin.site.register(register)
admin.site.register(contact)
admin.site.register(products)