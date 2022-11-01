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
      path("contactUs",views.contact,name="contact"),
      # path("logout",views.home,name="logout"),
      path("tickets",views.tickets,name="tickets"),
      path("myTicket",views.Myticket,name="Myticket"),
       path("myTicket2",views.Myticket2,name="Myticket2"),
      path('delete', views.delete, name='delete'),
      path('delete1', views.delete1, name='delete1'),
      path('adminLog', views.admin, name='admin'),
      path('adminReg', views.adminReg, name='adminReg'),
      path('view/<int:id>', views.view, name='view'),
      path('view1/<int:id>', views.view1, name='view1'),
      path('myAcc', views.myAcc, name='myAcc'),
      path('myAcc1', views.myAcc1, name='myAcc1'),
      path("logout", views.log_out, name="logout"),
      path("filter",views.filter ,name="filter"),
      path("changePass",views.changePass ,name="changePass"),
      path("raised",views.raised ,name="raised"),
      path("view3/<int:id>",views.view3 ,name="view3"),
      path("chat",views.chat ,name="chat"),
      path('checkview', views.checkview, name='checkview'),
      path('<str:room>/', views.room, name='room'),
      path('send', views.send, name='send'),
      path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
      # path("grid",views.grid ,name="grid"),
      # path("back",views.back ,name="back"),
      # path('view1/view3/<int:id>', views.view3, name='view3'),
      
      # path('admin', views.delete, name='admin')
      # path("newTicket",views.newTicket,name="newTicket")
      
     # path("helpDesk",views.helpDesk,name="helpDesk")
]
