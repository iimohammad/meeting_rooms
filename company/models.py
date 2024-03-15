from django.db import models
from accounts.models import CustomUser
from .validators import phone_validator


class Company(models.Model):
    name = models.CharField(max_length=15,unique=True)
    phone = models.CharField(max_length=15, validators=[phone_validator], blank=True)
    address = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Team(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,unique=True)
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='managed_teams')
    permission = models.BooleanField(default=True)
    priority = models.PositiveSmallIntegerField(default=5)
    members = models.ManyToManyField(CustomUser, related_name='teams')

    def __str__(self):
        return self.name
