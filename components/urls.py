from django.urls import path,include
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register('component',componentViewset,basename='component')
router.register('componentEach',componentEachViewset,basename='componentEach')
router.register('customerdata',customerdataViewset,basename="customerdata")

urlpatterns=[
    path('api/v5/',include(router.urls)),
    path('owner/register',registerView.as_view(),name="owner/register"),
    path('owner/login',loginView.as_view(),name="owner/login"),
    path('owner/registerprofile',registerprofile.as_view(),name='owner/registerprofile')
]

