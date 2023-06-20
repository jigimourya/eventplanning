from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser
from django.db import models

from event import settings


#from djangofrom tkinter.tix import MAX.conf import settings


class UserProfile(models.Model):
    # Other fields in your model
    your_school = models.CharField(max_length=50, choices=settings.PROGRAMMING_LANGUAGES)

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    systemid = models.CharField(max_length=10)

'''
class UserProfile(models.Model):
    # Other fields in your model
    your_school = models.CharField(max_length=50, choices=settings.PROGRAMMING_LANGUAGES)

class CustomUser(AbstractUser):
    
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    systemid = models.IntegerField(default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','password','systemid']
    @property
    def is_anonymous(self):
        return False

    # Override the default is_authenticated property
    @property
    def is_authenticated(self):
        return True
'''
class Organiser(models.Model):
    
    event_type = models.CharField(max_length=50, choices=settings.EVENT_TYPE)
    name_of_event = models.CharField(max_length=200)
    description = models.TextField(max_length = 200)
    department = models.CharField(max_length=50, choices=settings.PROGRAMMING_LANGUAGES)
    for_batch = models.CharField(max_length=50, choices=settings.BATCH)
    date = models.DateField()
    venue = models.CharField(max_length=200)
    time = models.TimeField()
    mode = models.CharField(max_length=50, choices=settings.MODE)
    user = models.CharField(max_length=50)
    organiser_name = models.CharField(max_length=200)
    organiser_phone = models.CharField(max_length=200)
    organiser_email = models.CharField(max_length=200)
    last_date_to_register = models.DateField(max_length=200)


