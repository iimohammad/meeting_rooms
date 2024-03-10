from django.db import models
from django.contrib.auth import get_user_model
from authentication.models import CustomUser


class Team(models.Model):
    status_Teams = (
        ('Active', 'Active'),
        ('Inactive','Inactive')
    )
    members = models.ManyToManyField(CustomUser, related_name='members_team' ,on_delete=models.CASCADE)
    Team_name = models.CharField(max_length=30)
    Team_manager = models.OneToOneField(CustomUser, related_name='mamager_of_team')
    status = models.CharField(max_length= 20, choices = status_Teams)
    
    def __str__(self):
        return self.Team_name


class company(models.Model):
    Teams = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField(max_length= 30)