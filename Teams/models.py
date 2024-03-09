from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model

class TeamStatus(models.TextChoices):
    active = 'active', 'Team can select'
    unactive = 'unactive', "Can't select"


class Team(models.Model):
    members = models.ManyToManyField(to=user, on_delete=models.CASCADE)
    Team_name = models.CharField()
    Team_manager = models.OneToOneField(user)
    status = models.CharField(max_length= 16, choice = TeamStatus.choices)


class company(models.Model):
    Teams = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField()
