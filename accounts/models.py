from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import phone_validator

class CustomUser(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        UNSET = 'MF', 'Unset'

    phone = models.CharField(max_length=15, validators=[phone_validator], blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.UNSET)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/')

class OTPCode(models.Model):
    email = models.CharField(max_length=255)
    code = models.CharField(max_length=6)

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')

class Author(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='author_profile')
    bio = models.TextField()
