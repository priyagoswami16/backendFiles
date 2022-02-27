from django.shortcuts import render
from home.models import test

# Create your views here.
def Home3(request):

    data = test.objects.all()
    context = {'data': data}
    if request.method == "POST":
        First_Name = request.POST.get("first_name")
        Last_Name = request.POST.get("last_name")
        best = test.objects.create(fname=First_Name,lname=Last_Name)
        best.save()
        return render(request, "index.html", context)
