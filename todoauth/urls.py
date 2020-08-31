from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns=[
    path('api_get',api_get,name="api_get"),
    path('register',RegisterView.as_view(),name="RegisterView"),
    path('login',loginView.as_view(),name="loginView"),
    path('logout',logoutView.as_view(),name="logoutView")
]
