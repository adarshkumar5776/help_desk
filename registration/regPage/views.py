from email import message
import re
from sre_parse import State
from token import RIGHTSHIFTEQUAL
from turtle import title
from xmlrpc.client import DateTime
from django.shortcuts import render,redirect
from django.contrib import messages
# from django.contrib.auth.models import User, auth
from regPage.models import regData
from django.contrib.auth.models import User
from regPage.models import Ticket





# from .models import City

# def load_cities(request):
#     country_id = request.GET.get('country_id')
#     cities = City.objects.filter(country_id=country_id).all()
#     return render(request, 'register.html', {'cities': cities})
# return JsonResponse(list(cities.values('id', 'name')), safe=False)

# def helpDesk(request):
#     return render(request, 'helpDesk.html')
def tickets(request):
    if request.method=="POST":
        title=request.POST.get('title')
        status=request.POST.get('status')
        priority=request.POST.get('Priority')
        description=request.POST.get('description')
        saverec = Ticket(title=title,priority=priority,description=description,status=status)
        saverec.save()
        return render(request,'home.html')
    else:   
         return render(request,'raiseTicket.html')

def Myticket(request):
    return render(request,'myTicket.html')   

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        
        username =request.POST['username']
        # password =request.POST['password']
        try:
            userDetails=0
            userDetails=regData.objects.get(username=request.POST['username'],password=request.POST['password'])
            return render(request,'home.html',{'userDetails':userDetails,'username':username})
        except regData.DoesNotExist as e:
            #  messages.info(request,'Invalid Credentials')
             return render(request,'login.html' )

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
            
     

def logout(request):
    return render(request,'home.html')

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
                elif len(mobile_no)!=12:
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



