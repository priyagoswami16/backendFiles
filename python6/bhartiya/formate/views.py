from django.shortcuts import render
from .models import resform
# from .form import registerform

# Create your views here.

def home2(request):
    # data = 'my name is priya'
    # context = {'data': data}

    # data = Forms.objects.all()
    # context = {'data': data}

    data = resform.objects.all()
    # context = {'data': data}
    if request.method == "POST":
        First_Name = request.POST("First_Name")
        Last_Name = request.POST("Last_Name")
        # Father_Name = request.POST.get("father_name")
        # Mother_Name = request.POST.get("mother_name")
        # Dob = request.POST.get("dob")
        # Mobile = request.POST.get("mobile")
        # Email = request.POST.get("email")
        # Address = request.POST.get("address")
        # Gender = request.POST.get("gender")
        # State = request.POST.get("state")
        # City = request.POST.get("city")
        # Pin_Code = request.POST.get("pin_code")
        # test = Forms.objects.create(first_name=First_Name,last_name=Last_Name,fathert_name=Father_Name,mother_name=Mother_Name, email=Email, address=Address,
        # pin_code=Pin_Code,dob=Dob,mobile=Mobile, gender=Gender, state= State, city=City )
        test = resform(First_Name=First_Name,Last_Name=Last_Name)
        test.save()
    return render(request, "index.html",{'data':data})
