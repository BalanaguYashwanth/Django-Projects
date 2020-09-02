from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns=[
    path('customerregister',customerregisterView.as_view(),name="customerregister"),
    path('customerlogin',customerloginView.as_view(),name="customerlogin"),
    path('customerprofile',customeruserprofileview.as_view(),name="customerprofile"),
    path('registercustomerdata',registercutomerdata.as_view(),name="registercustomerdata"),
    url(r'^deletecustomerprofile/(?P<id>\d+)/$',deletecustomerprofile.as_view(),name="deletecustomerprofile"),
    path('customerrequest',customerrequestView.as_view(),name="customerrequest")
]

