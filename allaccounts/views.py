from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def basex(request):
    return render(request,'all.html')


@csrf_exempt
def register(request):
    if request.method=="POST":
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        pg_id=request.POST['pgopt']
        if password==password1:
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.save()
            allprofiles.objects.create(user=user,pg_id=pg_id)
            return redirect(login)
        else:
            messages.info(request,'password is wrong once check')
            return redirect(register)
    else:
        return render(request,'allregisters.html')


@csrf_exempt
def login(request):

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(basex)
        else:
            messages.info(request,"Invalid Login Username & Password")
            return redirect(login)
    else:
        return render(request,'allloginforms.html')

def logout(request):
    auth.logout(request)
    return redirect(login)




        











