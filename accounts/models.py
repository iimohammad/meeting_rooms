from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import phone_validator


class CustomUser(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        UNSET = 'MF', 'Unset'

    class readonly(models.TextChoices):
        CompanyCEO = 'Company CEO', 'Company CEO'
        Member = 'Member', 'member'

    phone = models.CharField(max_length=15, validators=[phone_validator], blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.UNSET)
    CompanyManager = models.CharField(max_length=15, choices=readonly.choices, default=readonly.Member,blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class OTPCode(models.Model):
    email = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
