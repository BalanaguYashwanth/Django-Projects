from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns=[
    path('userprofile',userprofileView.as_view(),name="userprofie"),
    path('register',registers.as_view(),name="register"),
    path('login',logins.as_view(),name="login"),
    path('mainuserprofile',mainuserprofile.as_view(),name="mainuserprofile"),
    path('allprofiles',allprofiles.as_view(),name="allprofiles"),
    path('userbooking',userbookingsView.as_view(),name="userbooking"),
    #url(r'^userprofile_delete/(?P<id>\d+)/$',userprofileView_one.as_view,name="userprofile_delete")
]
    