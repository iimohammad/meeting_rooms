from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model
class Team(models.Model):
    members = models.ForeignKey(user, on_delete=models.CASCADE)
    Team_name = models.CharField()
    Team_manager = models.CharField()


class company(models.Model):
    Teams = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField()