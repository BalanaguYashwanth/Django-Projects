from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import details

# Create your views here.

def home(request):
    #return render(request,"home.html")
    return render(request,"file.html")

def data(request):
    if request.method=="POST":
        user=request.POST['user']
        phonenumber=request.POST['phonenumber']
        details.objects.create(phonenumber=phonenumber,user=user)
        all=details.objects.all()
        return redirect(home)
    else:
        all=details.objects.all()
        return render(request,"data1.html",{'all':all})
