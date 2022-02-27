from multiprocessing import context
# from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student, products
from .form import studentform
from .form import productsform

# Create your views here.

def index(request):
    data = "my name is priya"
    context = {'data': data}
    return render(request,"index.html", context)

def students(request):
    # data = student.objects.all()
    # context = {'data': data}
     
    form = studentform(request.POST) 
    context = {'form': form}
    if request.method == "POST":
      if form.is_valid():
         form.save()
         return HttpResponse('submitted') 
      else:
         return HttpResponse('not submitted')
    return render(request,"student.html", context)

def Home(request):
    return render(request, "navbarbase.html") 

def about(request):
    return render(request, "about.html")  

def contact(request):
    return render(request, "contact.html")  

def shop(request):
    return render(request, "shop.html")  

def slider(request):
    return render(request, "slider.html")   

def ecom(request):
    data = products.objects.all()
    context = {'data': data}
    return render(request, "ecom.html",context)  

def detail(request, id):
    data = products.objects.get(id = id)
    context = {'data': data}
    if request.method == 'POST':
        data.delete()
        return redirect('/ecom')
        pass
    return render(request, "details.html" ,context)                        

def update(request, id):
    var = products.objects.get(id = id) 
    form = productsform(instance=var)   
    if request.method == "POST":
        form = productsform(request.POST)
        name = request.POST['name']
        price = request.POST['price']
        img = request.POST['img']
        update = var
        update.name = name
        update.price = price
        update.img = img
        update.save()
        # return redirect('/ecom')
    return render(request, "update.html",{'form': form}) 