from enum import auto
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser
from django.db import models
from event import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import os
from django.core import validators




class UserProfile(models.Model):
    # Other fields in your model
    your_school = models.CharField(max_length=50, choices=settings.PROGRAMMING_LANGUAGES)



class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    systemid = models.CharField(max_length=10)

    
class Category(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    category_name = models.CharField(max_length=200)
    creation_date = models.DateField()

class Department(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    department_name = models.CharField(max_length=200)
    creation_date = models.DateField()

class Organiser(models.Model):

    category = Category.objects.all()

    catList = list()
    for cat in category:
        catName = cat.category_name
        catTuple = (catName, catName)
        catList.append(catTuple)

    department = Department.objects.all()
    deptList = list()
    for dept in department:
        deptName = dept.department_name
        deptTuple = (deptName, deptName)
        deptList.append(deptTuple)

    id = models.BigAutoField(primary_key=True, unique=True)
    user_id = models.BigIntegerField(default = 0)
    #event_type = models.CharField(max_length=50, choices=settings.EVENT_TYPE)
    event_type = models.CharField(max_length=50, choices=catList)
    name_of_event = models.CharField(max_length=200)
    description = models.TextField(max_length = 200)
    department = models.CharField(max_length=50, choices=deptList)
    for_batch = models.CharField(max_length=50, choices=settings.BATCH)
    event_date = models.DateField()
    venue = models.CharField(max_length=200)
    time = models.TimeField()
    mode = models.CharField(max_length=50, choices=settings.MODE)
    organiser_name = models.CharField(max_length=200)
    organiser_phone = models.CharField(max_length=200)
    organiser_email = models.EmailField(max_length=254, validators=[validators.EmailValidator(message="Invalid Email")])
    last_date_to_register = models.DateField(max_length=200)
    avatar = models.ImageField(upload_to='media/')
    thumbnail = models.CharField(max_length=255, blank=True)


    def get_year(self):
        return self.event_date.year


def generate_thumbnail(sender, instance, created, **kwargs):
    if created or instance.image != instance.thumbnail:
        # Open the original image
        image = Image.open(instance.image.path)
        
        # Generate a thumbnail (you can adjust the size as needed)
        thumbnail_size = (200, 200)
        image.thumbnail(thumbnail_size)
        
        # Save the thumbnail
        thumbnail_path = f'thumbnails/{instance.image.name}'
        thumbnail_full_path = os.path.join(settings.MEDIA_ROOT, thumbnail_path)
        image.save(thumbnail_full_path)
        
        # Update the thumbnail field in the model
        instance.thumbnail = thumbnail_path
        instance.save()


