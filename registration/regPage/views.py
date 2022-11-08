from email import message
import email
import http
from http.client import HTTPResponse
from multiprocessing import context
from datetime import datetime

from sre_parse import State
from time import time
from token import RIGHTSHIFTEQUAL
import datetime
from unicodedata import name
from xml.etree.ElementTree import Comment
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from regPage.models import regData, user_admin
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from regPage.models import Ticket
from regPage.models import comments
from regPage.models import activeUser
from regPage.models import contactUs
from django.contrib.auth import authenticate,login,logout
from django.utils.crypto import get_random_string
import random
from regPage.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password





# from .models import City

# def load_cities(request):
#     country_id = request.GET.get('country_id')
#     cities = City.objects.filter(country_id=country_id).all()
#     return render(request, 'register.html', {'cities': cities})
# return JsonResponse(list(cities.values('id', 'name')), safe=False)

# def helpDesk(request):
#     return render(request, 'helpDesk.html')

# def view3(request,id):
#     if request.method=="POST":
#         ticket_id=id
#         print(ticket_id)
#         comment=request.POST.get('comment')
#         saverec=comments(Comments=comment,ticket_id_id=ticket_id)
#         saverec.save()
#         return HttpResponseRedirect("") 
#     else:
#         return render(request,'comment.html')
# def back(request):
#   next = request.POST.get('next', '/')
#   return HttpResponseRedirect(next)


# ------------------------------------------------------------------------------

# def checkview1(request):
#     if request.method=="POST":
#       room = request.POST['room_name']
#       username = request.POST['username']
      
        
#     if Room.objects.filter(name=room).exists():
#              return redirect('/'+room+'/?username='+username)
            
#     else:
#              new_room = Room.objects.create(name=room)
#              new_room.save()
#              return redirect('/'+room+'/?username='+username)

# def checkview(request):
#     if request.method=="POST":
#       room = request.POST['room_name']
#       username = request.POST['username']
      
#     id=request.user.id
#     emp=Ticket.objects.get(appli_id=id)
#     emp2=regData.objects.get(pk=id)
    
#     if emp.ticket_id==room:
#         if emp2.username==username:
#             if Room.objects.filter(name=room).exists():
#             #  return redirect('/'+room+'/?username='+username)
#              return redirect('/'+room+'/?username='+username)
            
#             else:
#              new_room = Room.objects.create(name=room)
#              new_room.save()
#              return redirect('/'+room+'/?username='+username)
#         else:
#             return render(request,'home.html')
#     else:
#             return render(request,'home.html')

# def room(request, room):
    
#     username = request.GET.get('username')
#     print(username)
#     print(room)
#     room_details = Room.objects.get(name=room)
#     print(room_details.id)
#     return render(request, 'room.html', {
#         'username': username,
#         'room': room,
#         'room_details': room_details
#     })


# def send(request):
#     if request.method=='POST':
#        message = request.POST['message']
#        username = request.POST['username']
#        room_id = request.POST['room_id']

#        new_message = Message.objects.create(value=message, user=username, room=room_id)
#        new_message.save()
#        return HttpResponse('Message sent successfully')

# def getMessages(request, room):
  
#     room_details = Room.objects.get(name=room)
#     print(room_details.id)
#     messages = Message.objects.filter(room=room_details.id)
#     return JsonResponse({"messages":list(messages.values())})

# def chat1(request):
#     return render(request,'home123.html')
    
# def chat(request):
#     return render(request,'home.html')

def myAcc1(request):
    acc=True
    myAcc=user_admin.objects.all()
   
    return render(request,'myAccount.html',{'myAcc':myAcc,'acc':acc})

def view3(request,id):
    print(id)
    contacts=contactUs.objects.get(id=id)
    print(contacts.name)
    return render(request,'view3.html',{'contacts':contacts})

def raised(request):
    data=contactUs.objects.all()
    return render(request,'raised.html',{'data':data})

def contact(request):
    if request.method=='POST':
        id1=request.user.id
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneNo')
        message=request.POST.get('message')
        print(name)
        count=contactUs(contact_id_id=id1,name=name,email=email,mobile_no=phoneno,message=message)
        count.save()
        return render(request,"contactUs.html")
    else:
        return render(request,"contactUs.html")

def changePass(request):
    if request.method=="POST":
        id=request.user.id
        curr=regData.objects.get(pk=id)
        old=request.POST.get('oldPass')
        new=request.POST.get('newPass')
        retype=request.POST.get('retypePass')
        currPass=request.user.password
        print(curr.password)
        # print(currPass)
        print(new)
        if(old==currPass):
            if new==retype:
                curr.password=new
                curr.save()
                return HttpResponseRedirect("changePass")
            else:
                  return HttpResponseRedirect("changePass")
        else:
            return HttpResponseRedirect("changePass")
    else:    
        return render(request,'changePassword.html')


def filter(request):
    if request.method == "POST":
        priority=request.POST.get('Priority')
        status=request.POST.get('status')
        print(status)

        data=Ticket.objects.all()
        filt=True
        return render(request,'grid.html',{'priority':priority,'status':status,'filt':filt,'data':data})
    else:
    #   print('hello')
        return render(request,'filter.html')



def register(request):
    return render(request,'register.html')

def myAcc(request):
    # users = request.user.ticket_set.filter(appli_id = request.user.id)
    count=Ticket.objects.filter(appli_id=request.user.id).count()
    return render (request,'myAccount.html',{'count':count})


def view(request, id):
      

     users = request.user.ticket_set.filter(appli_id = request.user.id)

     com=comments.objects.filter(ticket_id=id)
     ticket = users.get(id = id)
    
     return render(request,'view2.html',{'ticket':ticket ,'com':com})

def view1(request,id):
    if request.method=="POST":
        
        emp = Ticket.objects.get(pk = id)
        emp.status = 'close'
        emp.save()
    
        ticket_id=id
        print(ticket_id)
        comment=request.POST.get('comment')
        saverec=comments(Comments=comment,ticket_id_id=ticket_id)
        saverec.save()
        admin =True
        ticket = Ticket.objects.get(id = id)
        return render(request,'view2.html',{'ticket':ticket, 'admin': admin})
      
    else:
   
    # datas=Ticket.objects.all()
     ticket = Ticket.objects.get(id = id)
    # datas = Ticket.objects.filter(appli_id=y)
     admin =True
     return render(request,"view2.html",{'ticket':ticket, 'admin': admin})

def delete1(request):
    if request.method == "POST":
       identity = request.POST.get("delete1")
       member = contactUs.objects.get(id=int(identity))

       member.delete()
       return HttpResponseRedirect("raised")
    return render(request,'raised.html')
   


def delete(request):
    if request.method == "POST":
      identity = request.POST.get("delete")
    #   print(identity)
      member = Ticket.objects.get(id=int(identity))
      member.delete()
      return HttpResponseRedirect("myTicket")
    return render(request , 'myticket.html')

def admin(request):
    if request.method == 'POST':
        try:
            usernames=request.POST['username']
            # password =request.POST['password']
            users=user_admin.objects.get(username=request.POST['username'],password=request.POST['password'])
            # login(request,users)
            return render(request,'home1.html',{'users':users,'usernames':usernames})
        except:
            return redirect('admin')
    return render(request,'adminLogin.html')

def adminReg(request):
     if request.method=="POST":
            full_name=request.POST.get('full_name')
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            saverecord = user_admin(first_name=full_name,username=username,email=email,password=password)
            saverecord.save()
            return render(request,'adminLogin.html')
            
     else:
          return render(request,'adminReg.html')

# def user_admin(request):
#     data = regData.objects.all()
#     return render(request,"admin.html",{"data":data})

def tickets(request):
    if request.method=="POST":
        appli = request.user.id
        title=request.POST.get('title')
        issueType=request.POST.get('issue')
        status=request.POST.get('status')
        priority=request.POST.get('Priority')
        description=request.POST.get('description')
        unique_id = get_random_string(length=5)
        unique_id.upper()
        print(unique_id)
       
        saverec = Ticket(ticket_id=unique_id,appli_id = appli, title=title,issueType=issueType, priority=priority,description=description,status=status)
        saverec.save()
        return render(request,'raiseTicket2.html')
        # return HttpResponseRedirect('tickets')
    else:    
         return render(request,'raiseTicket2.html')

def Myticket(request):
    # current_datetime = datetime.datetime.now()
    
    
    
    data=Ticket.objects.all()
    # datas=regData.objects.all()
   
    return render(request,'grid.html',{'data':data}) 
      
def Myticket2(request):
    # current_datetime = datetime.datetime.now()
    data=Ticket.objects.all()
    # datas=regData.objects.all()
    userData=True
    return render(request,'grid.html',{'data':data,'userData':userData}) 

def home(request):
    return render(request,'home1.html')

def log_in(request):


    if request.method == 'POST':
        try:
            
            username =request.POST['username']
            password=request.POST['password']
            # userdetails=regData.objects.get(username=request.POST['username'],password=request.POST['password'])
            userdetails=authenticate(request,username=username,password=password)
            login(request, userdetails)
            # return redirect('home')
            t1=datetime.datetime.now().time().replace(microsecond=0)
            count=Ticket.objects.filter(appli_id=request.user.id).count()
            user_id=request.user.id
            savet=activeUser(login_time=t1,time_id=user_id)
            savet.save()
            return render(request,'home1.html',{'userDetails':userdetails,'username':username,'count':count})
        except regData.DoesNotExist as e:
            return render(request,'login.html')

        # username =request.POST['username']
        # password =request.POST['password']
        # user = regData.objects.get(username=username)
        # if user.password == password:
        #     login(request, user)
        #     # return redirect('home')
        #     t1=datetime.datetime.now().time().replace(microsecond=0)

        #     user_id=request.user.id
        #     savet=activeUser(login_time=t1,time_id=user_id)
        #     savet.save()
        #     return render(request,'home.html',{'userDetails':user,'username':username})
           
        # else:
        #     # messages.error(request +"Username/Password is invalid")
        #     return redirect()
   
    


    else:
        return render(request,'login.html')
          


        # username0=regData.objects.get(username)
        # password0=regData.objects.get(password)

        # user=regData.authenticate(username=username,password=password)
        # if username==username0 and password==password0:
        #     return render(request,'register.html')
        # else:
        #     return render(request,'index.html')
            



        # if user is not None:
        #     regData.login(request,user)
        #     return redirect('register')
        # else:
        #     messages.info(request,'invalid credentials')
        #     return redirect('login')
            
  

# def logout(request):
#     auth.logout(request)
#     return redirect("/")
    # return render(request,'home.html')

def log_out(request):
   
    user_id=request.user.id
    print(user_id)
    emp = activeUser.objects.get(pk=user_id)
    emp.logout_time=datetime.datetime.now().time().replace(microsecond=0)

    
    t1=str(emp.login_time)
    t2=str(emp.logout_time)
    
    temp1=datetime.datetime.strptime(t1,'%H:%M:%S')
    temp2=datetime.datetime.strptime(t2,'%H:%M:%S')
    diff=temp2-temp1
    sec=(diff.total_seconds())
    sec1= str(datetime.timedelta(seconds = sec))
    print(sec1)
    # user_id=request.user.id
    # emp = activeUser.objects.get(pk=user_id)
   
    emp.TotalActiveTime=sec1
    emp.save()

    # newTime=datetime.datetime.strptime(sec1,'%H:%M:%S')
    # print(newTime)
    # print(t1)
    # print(t2)
    
    # savet=activeUser(request.POST,logout_time=t2)
    # savet.save()
    logout(request)
    return redirect('/')
    # return(logout)
      

def register(request):
    if request.method=="POST":
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            username=request.POST.get('username')
            email=request.POST.get('email')
            address=request.POST.get('address')
            city=request.POST.get('city')
            state=request.POST.get('state')
            country=request.POST.get('country')
            mobile_no=request.POST.get('mobile_no')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            # passwordn=make_password(password1)

            if password1==password2 :
                if regData.objects.filter(username=username).exists():
                    messages.info(request,'Username Taken')
                    return redirect('register')
                elif regData.objects.filter(email=email).exists():
                    messages.info(request,'email Taken')
                    return redirect('register')
                elif len(mobile_no)!=10:
                    messages.info(request,"Invalid Mobile Number")
                    return redirect('register')
                else:
                    saverecord = regData(first_name=first_name,last_name=last_name,username=username,email=email,address=address,state=state,city=city,country=country,mobile_no=mobile_no,password=make_password(password1))
                    saverecord.save()
                    return render(request,'login.html')
            else:
                messages.info(request,'Invalid Credential')
                return redirect('register')
            # messages.success(request + saverecord.first_name+' Is successfully registered...')
            
    else:
            return render(request,'register.html')

# def register(request):
#     if request.method=="POST":
#         if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('username') and request.POST.get('email') and request.POST.get('address') and request.POST.get('city') and request.POST.get('state') and request.POST.get('country') and request.POST.get(' mobile_no'):
#             saverecord=regData()
#             saverecord.first_name=request.POST('first_name')
#             saverecord.last_name=request.POST('last_name')
#             saverecord.username=request.POST('username')
#             saverecord.email=request.POST('email')
#             saverecord.address=request.POST('address')
#             saverecord.city=request.POST('city')
#             saverecord.state=request.POST('state')
#             saverecord.country=request.POST('country')
#             saverecord.mobile_no=request.POST('mobile_no')
#             saverecord.save()
#             # messages.success(request + saverecord.first_name+' Is successfully registered...')
#             return redirect('register')
#     else:
#             return render(request,'register.html')
            
           


    
    # if request.method == 'POST':
    #     first_name=request.POST['first_name']
    #     last_name=request.POST['last_name']
    #     username=request.POST['username']
    #     password1=request.POST['password1']
    #     password2=request.POST['password2']
    #     email=request.POST['email']
    #     City=request.POST['city']
    #     State=request.POST['state']
    #     Country=request.POST['country']
    #     Address=request.POST['address']
    #     # mobile_no=request.POST['mobile_no']
    

    #     if password1==password2:
            # if User.objects.filter(username=username).exists():
            #     # messages.info(request,'Username Taken')
            #     return redirect('register')
            # elif User.objects.filter(email=email).exists():
            #     # messages.info(request,'email Taken')
            #     return redirect('register')
    #         else:
    #             user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name,city=City,state=State,country=Country,address=Address)
    #             user.save();
    #             return redirect('register')
    #             # print('user created')
    #             # return redirect('login')
    #     else:
    #         # print('password not watching..')
    #         return redirect('register')
    # else:
    #     return render(request,'register.html')

