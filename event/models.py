from django.contrib.auth.models import AbstractUser
from django.db import models

from event import settings


#from djangofrom tkinter.tix import MAX.conf import settings

class UserProfile(models.Model):
    # Other fields in your model
    your_school = models.CharField(max_length=50, choices=settings.PROGRAMMING_LANGUAGES)

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    system_id = models.CharField(max_length=10)

class Organiser(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title

