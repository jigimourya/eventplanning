from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    systemid = models.CharField(max_length=10)

#class CustomUser2(AbstractUser):
   # systemid = models.CharField(max_length=10)