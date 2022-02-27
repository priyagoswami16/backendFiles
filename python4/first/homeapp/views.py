from multiprocessing import context
from django.shortcuts import render
from .models import student

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def photo(request):
    return render(request,'photo.html')

# def contact(request):
#     data = student.objects.all()
#     context = {'data':data}
#     return render(request,'contact.html',context)    

# def present(request):
#     data = student.objects.all()
#     context = {'data':data}
#     return render(request,'index2.html',context)       
 
def present(request):
    data = student.objects.all()
    context = {'data': data}
    if request.method == "POST":
        Name = request.POST.get("name")
        Email = request.POST.get("email")
        Massage = request.POST.get("massage")
        test = student.objects.create(name=Name, email=Email, massage=Massage)
        test.save()
    return render(request,'index2.html',context) 

def contact(request):
    data = student.objects.all()
    context = {'data': data}
    if request.method == "POST":
        Name = request.POST.get("name")
        Email = request.POST.get("email")
        Massage = request.POST.get("massage")
        test = student.objects.create(name=Name, email=Email, massage=Massage)
        test.save()
    return render(request,'contact.html',context)           

