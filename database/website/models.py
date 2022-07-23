from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Website(models.Model):
    first_name= models.CharField(max_length=20, unique=True)
    last_name= models.CharField(max_length=20, unique=True)
    create_username= models.CharField(max_length=20, unique=True)
    create_password= models.CharField(max_length=20, unique=True)
    
