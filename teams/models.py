from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from authentication.models import CustomUser


class Company(models.Model):
    name = models.CharField(max_length=15)
    address = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Team(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    def get_absolute_url(self, status):
        if status == 'show_team_members':
            return reverse('teams:show_team_members', args=(self.id,))
        elif status == 'delete_team':
            return reverse('teams:delete_team', args=(self.id,))
        elif status == 'show_team_reservations':
            return reverse('teams:show_team_reservations', args=(self.id,))


class Manager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    access = models.BooleanField(default=True)


class MeetingRoom(models.Model):
    name = models.CharField(max_length=15)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.company.name} Company: {self.name} Room'


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('p', 'Pending'),
        ('i', 'In Progress'),
        ('d', 'Done'),
    ]

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    meeting_room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField()
    duration = models.DurationField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')

    def __str__(self):
        return f'Reservation {self.id}: Team {self.team.name}, Status {self.status}'
