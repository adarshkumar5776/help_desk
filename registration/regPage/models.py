from email import message
from email.policy import default
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class regData(AbstractUser):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # city = models.ForeignKey(City, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    mobile_no= models.BigIntegerField()
    password=models.CharField(max_length= 200)

class contactUs(models.Model):
    contact_id=models.ForeignKey(regData,on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile_no= models.BigIntegerField()
    message=models.TextField(max_length=200)
    

class activeUser(models.Model):
    time=models.ForeignKey(regData,on_delete=models.CASCADE,primary_key=True)
    login_time=models.TimeField(null=True)
    logout_time=models.TimeField(null=True)
    TotalActiveTime=models.TimeField(null=True)
    # TotalActiveTime1=models.CharField(max_length=100,null=True)



class Ticket(models.Model):
    appli=models.ForeignKey(regData,on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    issueType=models.CharField(max_length=100)
    priority=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
    dateTime = models.DateTimeField(default=timezone.now)

class user_admin(models.Model):
    
    first_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password=models.CharField(max_length= 200)

class comments(models.Model):
    Comments=models.TextField()
    ticket_id=models.ForeignKey(Ticket,on_delete=models.CASCADE)

class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    
    
    
