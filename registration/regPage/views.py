from email import message
import http
from http.client import HTTPResponse
from multiprocessing import context

from sre_parse import State
from token import RIGHTSHIFTEQUAL
import datetime
from xml.etree.ElementTree import Comment
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from regPage.models import regData, user_admin
from django.contrib.auth.models import User
from django.contrib.auth import login
from regPage.models import Ticket
from regPage.models import comments
from django.contrib.auth import authenticate,login,logout






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



def myAcc(request):
    # users = request.user.ticket_set.filter(appli_id = request.user.id)
    count=Ticket.objects.filter(appli_id=request.user.id).count()
    return render (request,'myAccount.html',{'count':count})


def view(request, id):
      

     users = request.user.ticket_set.filter(appli_id = request.user.id)

     com=comments.objects.filter(ticket_id=id)
     ticket = users.get(id = id)
    
     return render(request,'view.html',{'ticket':ticket ,'com':com})

def view1(request,id):
    if request.method=="POST":
        
        emp = Ticket.objects.get(pk = id)
        emp.status = 'closed'
        emp.save()
    
        ticket_id=id
        print(ticket_id)
        comment=request.POST.get('comment')
        saverec=comments(Comments=comment,ticket_id_id=ticket_id)
        saverec.save()
        admin =True
        ticket = Ticket.objects.get(id = id)
        return render(request,'view.html',{'ticket':ticket, 'admin': admin})
      
    else:
   
    # datas=Ticket.objects.all()
     ticket = Ticket.objects.get(id = id)
    # datas = Ticket.objects.filter(appli_id=y)
     admin =True
     return render(request,'view.html',{'ticket':ticket, 'admin': admin})

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
            return render(request,'home.html',{'users':users,'usernames':usernames})
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
        status=request.POST.get('status')
        priority=request.POST.get('Priority')
        description=request.POST.get('description')
        saverec = Ticket(appli_id = appli, title=title,priority=priority,description=description,status=status)
        saverec.save()
        return render(request,'raiseTicket.html')
        # return HttpResponseRedirect('tickets')
    else:   
         return render(request,'raiseTicket.html')

def Myticket(request):
    # current_datetime = datetime.datetime.now()
    
    
    
    data=Ticket.objects.all()
    # datas=regData.objects.all()
   
    return render(request,'myTicket.html',{'data':data}) 
      
def Myticket2(request):
    # current_datetime = datetime.datetime.now()
    data=Ticket.objects.all()
    # datas=regData.objects.all()
    userData=True
    return render(request,'myTicket.html',{'data':data,'userData':userData}) 

def home(request):
    return render(request,'home.html')

def log_in(request):
    
    if request.method == 'POST':
    #     try:
    #         username =request.POST['username']
    #         userdetails=regData.objects.get(username=request.POST['username'],password=request.POST['password'])
    #         return render(request,'home.html',{'userDetails':userdetails,'username':username})
    #     except regData.DoesNotExist as e:
    #         return render(request,'login.html')

        username =request.POST['username']
        password =request.POST['password']
        user = regData.objects.get(username=username)
        if user.password == password:
            login(request, user)
            # return redirect('home')
            return render(request,'home.html',{'userDetails':user,'username':username})
        else:
            # messages.error(request +"Username/Password is invalid")
            return HttpResponseRedirect("login")


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
def logout(request):
  logout(request)
      

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
                    saverecord = regData(first_name=first_name,last_name=last_name,username=username,email=email,address=address,state=state,city=city,country=country,mobile_no=mobile_no,password=password1)
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



