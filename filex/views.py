from django.shortcuts import render,redirect
from .models import details
from filex.models import orderdetails
from filex.models import *
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def home(request):
    return render(request,'main.html')



def forms(request):
    return render(request,'forms.html')
    
def imageforms(request):
    return render(request,'imageforms.html')

def postimage(request):
    return render(request,'postimage.html')

def slidepostimage(request):
    return render(request,'slidepostimage.html')

def secondaryimages(request):
    return render(request,'secondaryimages.html')

def primaryimages(request):
    return render(request,'primaryimages.html')

def slideimage(request):
    return render(request,'fileimages.html')

def slideimages(request):
    return render(request,'slideimages.html')

def images(request):
    return render(request,'images.html')

def contactdatas(request):
    return render(request,'contactdatas.html')

def orderdatas(request):
    return render(request,"orderdatas.html")
