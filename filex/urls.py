from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('contactdatas',views.contactdatas,name="contactdatas"),
    path('orderdatas',views.orderdatas,name="orderdatas"),
    path('forms',views.forms,name="forms"),
    path('imageforms',views.imageforms,name="imageforms"),
    path('postimage',views.postimage,name="postimage"),
    path('images',views.images,name='images'),
    path('slideimage',views.slideimage,name="slideimage"),
    path('slideimages',views.slideimages,name="slideimages"),
    path('slidepostimage',views.slidepostimage,name="slidepostimage"),
    path('secondaryimages',views.secondaryimages,name="secondaryimages"),
    path('primaryimages',views.primaryimages,name="primaryimages"),

]

