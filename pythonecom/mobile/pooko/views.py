from django.shortcuts import render
from .models import Cruasal, Products, Categroy, Scrdile
from .form import ContactForm


# Create your views here.
def home(request):
    abb = Cruasal.objects.all()
    return render(request,'index.html',{'abb':abb})  


def contact(request):
    form = ContactForm(request.POST)
    if request.method == "POST":
       if form.is_valid():
          form.save()
    return render(request,'contact.html',{'form': form})         

def ecomproduct(request):
    data = Products.objects.all()
    return render(request,'product.html',{'data':data})     

def categry(request):
    cat = Categroy.objects.all()
    var = Scrdile.objects.all()
    return render(request,'categry.html',{'cat':cat,'var':var})            

def Detail(request, id):
    data = Products.objects.get(id = id)
    context = {'data': data}
    return render(request,'details.html', context) 


 