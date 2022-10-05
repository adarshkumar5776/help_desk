from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from regPage.models import regData

urlpatterns = [
      path("register",views.register,name="register"),
      path("login",views.login,name="login"),
      path("",views.home,name="home"),
      path("logout",views.home,name="logout")
      
     # path("helpDesk",views.helpDesk,name="helpDesk")
]