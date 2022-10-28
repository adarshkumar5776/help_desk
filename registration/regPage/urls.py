from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from regPage.models import regData
from django.contrib.auth.views import LogoutView 


urlpatterns = [
      path("register",views.register,name="register"),
      path("login",views.log_in,name="log_in"),
      path("",views.home,name="home"),
      # path("logout",views.home,name="logout"),
      path("tickets",views.tickets,name="tickets"),
      path("myTicket",views.Myticket,name="Myticket"),
       path("myTicket2",views.Myticket2,name="Myticket2"),
      path('delete', views.delete, name='delete'),
      path('adminLog', views.admin, name='admin'),
      path('adminReg', views.adminReg, name='adminReg'),
      path('view/<int:id>', views.view, name='view'),
      path('view1/<int:id>', views.view1, name='view1'),
      path('myAcc', views.myAcc, name='myAcc'),
      path("logout", views.log_out, name="logout"),
      path("filter",views.filter ,name="filter"),
      path("changePass",views.changePass ,name="changePass"),
      path("grid",views.grid ,name="grid"),
      # path("back",views.back ,name="back"),
      # path('view1/view3/<int:id>', views.view3, name='view3'),
      
      # path('admin', views.delete, name='admin')
      # path("newTicket",views.newTicket,name="newTicket")
      
     # path("helpDesk",views.helpDesk,name="helpDesk")
]
