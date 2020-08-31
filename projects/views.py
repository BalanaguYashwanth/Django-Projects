from django.shortcuts import render,redirect
from .models import *

def home(request):
    return render(request,'pgimages.html')

def all(request):
    return render(request,'all.html')

def firstpage(request):
    if request.method=="POST":
        pgname=request.POST["pgname"]
        location=request.POST["location"]
        pgdata.objects.create(pgname=pgname,location=location)
        all=pgdata.objects.all()
        return render(request,"firstpage.html",{"all":all})
    else:
        all=pgdata.objects.all()
        return  render(request,'middlepage.html',{"all":all})

def images(request):
    if request.method=="POST":
       fname=request.POST['fname']
       fid=request.POST['fid']
       picture= request.FILES['picture']
       filedata.objects.create(fname=fname,picture=picture,fid=fid) 
       all=filedata.objects.all()
       return render(request,'pgimagesx.html',{"all":all})
    else:
        all=filedata.objects.all()
        return render(request,'pgimagesx.html',{'all':all})

