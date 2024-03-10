# from django.db import models
# from django.contrib.auth import get_user_model


# User = get_user_model()

# class TeamStatus(models.TextChoices):
#     active = 'active', 'Team can select'
#     unactive = 'unactive', "Can't select"


# class Team(models.Model):
#     members = models.ManyToManyField(to=User)
#     Team_name = models.CharField(max_length=100)
#     Team_manager = models.OneToOneField(User, on_delete=models.CASCADE)
#     status = models.CharField(max_length=16, choices=TeamStatus.choices)


# class Company(models.Model):
#     Teams = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
#     company_name = models.CharField(max_length=100)
