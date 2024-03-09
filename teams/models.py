from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


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
        if status is 1:
            return reverse('teams:show_team_members', args=(self.id,))
        elif status is 2:
            return reverse('teams:delete_team', args=(self.id,))
        elif status is 3:
            return reverse('teams:show_team_reservations', args=(self.id,))


class CustomUser(AbstractUser):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=11)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Manager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)


class MeetingRoom(models.Model):
    name = models.CharField(max_length=15)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    available = models.BooleanField()

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
    start_datetime = models.DateTimeField()
    duration = models.TimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')

    def __str__(self):
        return f'Reservation {self.id}: Team {self.team.name}, Status {self.status}'
