from django.db import models
from django.contrib.auth.models import User, UserManager 


# Create your models here.
class CustomUser(User):
    """User with app settings."""
    phoneno = models.CharField(max_length=50, default='')    
    professional = models.CharField(max_length=50, default='')
    town = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='')
    worktype = models.CharField(max_length=50, default='')
    currentlyworking = models.CharField(max_length=50, default='')
    stafftype = models.CharField(max_length=50, default='')
    familyplaning = models.CharField(max_length=50, default='')
    providedit = models.CharField(max_length=50, default='')
    nurhitraining = models.CharField(max_length=50, default='')
    education = models.CharField(max_length=50, default='')
    religion = models.CharField(max_length=50, default='')
    sex = models.CharField(max_length=50, default='')
    age = models.CharField(max_length=50, default='')
    # Use UserManager to get the create_user method, etc.
    objects = UserManager()