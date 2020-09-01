"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from filex.api import *
from filex import api
from todo import api1
from todo.api1 import *
from opensourceauth.urls import *
# from todo import api
# from todo.api import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('todo.urls')),
    #path('',include('file.urls')),
    #path('',include('filex.urls')),
    #path('todo',include('todo.urls')),
    #path('',include('projects.urls')),
    #path('allaccounts/',include('allaccounts.urls')),
    #path('acccounts/',include('acccounts.urls')),
    #url(r'^api/v1/todo_api/$',(api.todo_api.as_view()),name="todoapi"),
    # url(r'^api/v1/detailed/$',(api.detailed.as_view()),name='detailed'),
    # url(r'^api/v1/Moredetail/(?P<id>\d+)/$',api.Moredetail.as_view(),name='Moredetail'),
    # url(r'^api/v1/orderdetailed/$',(api.orderdetailed.as_view()),name='orderdetailed'),
    # url(r'^api/v1/orderMoredetail/(?P<id>\d+)/$',api.orderMoredetail.as_view(),name='orderMoredetail'),

    # url(r'^api/v1/filesdatadetailed/$',api.filesdatadetailed.as_view(),name='filesdatadetailed'),
    # url(r'^api/v1/filesdataMoredetail/(?P<id>\d+)/$',api.filesdataMoredetail.as_view(),name='filesdataMoredetail'),


    # url(r'^api/v1/slidedatadetailed/$',api.slidedatadetailed.as_view(),name='slidedatadetailed'),
    # url(r'^api/v1/slidedataMoredetail/(?P<id>\d+)/$',api.slidedataMoredetail.as_view(),name='slidedataMoredetail'),
    # url(r'^api/v3/todo_api/$',api1.todo_api.as_view(),name="todo_api"),
    # url(r'^api/v3/todo_api_one/(?P<id>\d+)/$',api1.todo_api_one.as_view(),name="todo_api_one"),
    # url(r'^api/v3/logoutView/$',api1.logoutView.as_view(),name="logoutView"),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    #path('todoauth/',include('todoauth.urls')),
    #url(r'^api/v3/retriveToken/$',api2.retriveToken.as_view(),name="retriveToken"),
    url(r'^userprofile_delete/(?P<id>\d+)/$',userprofileView_one.as_view(),name="userprofile_delete"),
    path('opensourceauth/',include('opensourceauth.urls')),

]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

