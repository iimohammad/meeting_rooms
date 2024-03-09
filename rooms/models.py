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

class MeetingRoom(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    is_booked = models.BooleanField(default=False)

class Reservation(models.Model):
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()