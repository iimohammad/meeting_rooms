from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from .validators import phone_validator


User = get_user_model()


class Company(models.Model):
    name = models.CharField(max_length=15)
    phone = models.CharField(max_length=15, validators=[phone_validator], blank=True)
    address = models.CharField(max_length=120)
    def __str__(self):
        return self.name


class Team(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_teams')
    permission = models.BooleanField(default=True)
    priority = models.PositiveSmallIntegerField(default=5)
    members = models.ManyToManyField(User, related_name='teams')
    def __str__(self):
        return self.name

    def get_absolute_url(self, status):
        if status == 'show_team_members':
            return reverse('teams:show_team_members', args=(self.id,))
        elif status == 'delete_team':
            return reverse('teams:delete_team', args=(self.id,))
        elif status == 'show_team_reservations':
            return reverse('teams:show_team_reservations', args=(self.id,))





