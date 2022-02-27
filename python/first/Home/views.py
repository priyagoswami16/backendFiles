from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import student
from .models import contact
from .form import contactform
from .form import registerform
from .form import productsform
from .models import register,products
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail, EmailMessage
from first.settings import EMAIL_HOST_USER



# Create your views here.
def home(request):
    return render(request, 'index.html' )
  
def about(request):
    return render(request , 'about.html')

def photo(request):
    return render(request , 'photo.html')

def call(request):
    info = "hii I am developer" 
    context = {'key': info}
    return render(request, 'data.html', context)



def home2(request):
    data = student.objects.all()
    context = {'data': data}
    if request.method == "POST":
        Name = request.POST.get("name")
        Email = request.POST.get("email")
        Massage = request.POST.get("massage")
        test = student.objects.create(name=Name, email=Email, massage=Massage)
        test.save()
    return render(request, 'index2.html',context )
    

def home3(request):
    data = "i am diya"
    data1 = 4
    context = {'data': data,
    'data1': data1}          
    return render(request, 'diya.html',context)   

def home4(request):
    data = "my name is priya"
    context = {'data': data}          
    return render(request, 'priya.html',context) 


def login(request):
    form = UserCreationForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request,"login.html",{'form': form})

def rgister(request):
    form =  registerform(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse('submitted')
        else:
            return HttpResponse('not submitted')
    return render (request,"register.html",{'form':form})

def contacts(request):
      form = contactform(request.POST)
      if request.method == "POST":
        if form.is_valid():
            form.save()
      return render(request,"contact.html",{'form': form})


def ecom(request):
      data = products.objects.all()
      request.method == "POST"
      qry = request.POST.get('qry')
    #   var = products.objects.filter(name = qry)
    #   data = var 
      return render(request,"ecom.html",{'data':data})

def details(request, id):
    data = products.objects.get(id = id)
    context = {'data': data}
    if request.method == 'POST':
        data.delete()
        return redirect('/ecom')
        pass
    return render(request,"details.html",context)      

def update(request , id):
    var = products.objects.get(id = id)
    form = productsform( instance=var )
    if request.method == "POST":
        form = productsform(request.POST )
        name = request.POST['name']
        price = request.POST['price']
        img = request.POST['img']
        update = var
        update.name = name 
        update.price = price 
        update.img = img
        update.save()
        return HttpResponse('updated') 
    return render(request, 'update.html', {'form':form })


def sender(requset):

    if requset.method  == "POST":
       email = requset.POST.get('email')
       subject = requset.POST.get('subject')
       message = requset.POST.get('message')
       send_mail(subject,message, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently = False)
       send_mail(subject,message, EMAIL_HOST_USER, [email], fail_silently = False )          
    return render(requset, 'emailform.html')      

# def search(request):
#     request.method == "POST"
#     qry = request.POST.get('qry')
#     var = products.objects.filter(name = qry)
#     data = var  
#     return render(request,"search.html", {'data':data})
