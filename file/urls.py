from django.urls import path,include
from . import views
from rest_framework import routers
from .viewsets import *

router=routers.SimpleRouter()
router.register('details',detailsViewsets,basename="details")

urlpatterns = [
    path('',views.home,name="home"),
    path('data',views.data,name="data"),
    path('api/v1/',include(router.urls))
]
