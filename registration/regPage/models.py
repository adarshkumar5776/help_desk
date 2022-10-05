from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

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
    
    
