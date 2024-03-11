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
    token = models.CharField(max_length=64, blank=True, unique=True)  # Token field for token-based authentication

    def generate_token(self):
        """
        Generates a unique token for the user.
        """
        while True:
            token = secrets.token_urlsafe(32)  # Generate a random token
            if not CustomUser.objects.filter(token=token).exists():  # Check if the token is unique
                break  # Exit the loop if the token is unique
        self.token = token
        self.save()
    def invalidate_token(self):
        """
        Invalidates the user's token.
        """
        self.token = ""
        self.save()

class OTPCode(models.Model):
    email = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
