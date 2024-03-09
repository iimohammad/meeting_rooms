from django.db import models
from django.contrib.auth.models import AbstractUser
from .models import CustomUser


class Company(models.Model):
    name = models.CharField(max_length=15)
    address = models.CharField(max_length=120)


class Team(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    manager = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)


class CustomUser(AbstractUser):
    member_of = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=11)
    picture = models.FileField(null=True)


class MeetingRoom(models.Model):
    name = models.CharField(max_length=15)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    available = models.BinaryField()


class Reservation(models.Model):

    STATUS_CHOICES = [
        ('p', 'Pending'),
        ('i', 'In Progress'),
        ('d', 'Done'),
    ]
        
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    meeting_room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    duration = models.TimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')
