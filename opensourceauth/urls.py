from django.urls import path
from .views import *

urlpatterns=[
    path('userprofile',userprofileView.as_view(),name="userprofie"),
    path('register',registers.as_view(),name="register"),
    path('login',logins.as_view(),name="login")
]
