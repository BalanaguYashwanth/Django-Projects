from django.urls import path,include
from . import views

urlpatterns=[
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('basex',views.basex,name="basex"),
    path('logout',views.logout,name="logout"),
]
