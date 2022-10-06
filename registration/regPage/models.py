from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db import models
from django.conf import settings
from django.utils import timezone

# class Country(models.Model):
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name


# class City(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name


class regData(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # city = models.ForeignKey(City, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    mobile_no= models.BigIntegerField()
    password=models.CharField(max_length= 200)

class Ticket(models.Model):
    title = models.CharField(max_length=254)
    priority=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
     #check for default value
    # creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    # dateTime = models.DateTimeField(default=timezone.now)
    # lastUpdate = models.DateTimeField(auto_now=True)

    # States = (
    #     ('Waiting for response', 'Waiting for response'),
    #     ('Answered', 'Answered'),
    #     ('Closed', 'Closed'),
    # )
    # state = models.CharField(max_length=20, choices=States, default="Waiting for response")

    # Priorities = (
    #     ('Low', 'Low'),
    #     ('Medium', 'Medium'),
    #     ('High', 'High'),
    # )
    # priority = models.CharField(max_length=6, choices=Priorities, default=0)

    # def __str__(self):
    #     return self.title
    
    
