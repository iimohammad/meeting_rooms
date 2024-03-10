from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
        
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11)
    profile_image = models.ImageField(upload_to ='profile_images/')