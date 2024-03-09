from django.db import models
from django.contrib.auth import get_user_model




user = get_user_model

# class Team(models.Model):
#     members = models.ForeignKey(user, on_delete=models.CASCADE)
#     Team_name = models.CharField()
#     Team_manager = models.CharField()


# class company(models.Model):
#     Teams = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
#     company_name = models.CharField()``


class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200)

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class MeetingRoom(models.Model):
    room = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)

class Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)
    is_canceled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField(blank=True, null=True)
    score = models.IntegerField(null=True, blank=True)
    review = models.TextField(blank=True, null=True)
    otp = models.CharField(max_length=6)
    
class Review(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
