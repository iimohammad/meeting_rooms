from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone

user = get_user_model()


class MeetingRoom(models.Model):
    room_name = models.CharField(max_length=20)
    capacity = models.PositiveBigIntegerField()
    location = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)

    def is_available(self, date, start_time, end_time):
        if not self.available:
            return False

        # Check if there are any overlapping sessions
        overlapping_sessions = Sessions.objects.filter(
            meeting_room=self,
            date=date,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        return not overlapping_sessions.exists()


class Sessions(models.Model):
    team = models.ForeignKey('company.Team', on_delete=models.CASCADE)
    meeting_room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def is_past(self):
        return timezone.now() > timezone.datetime.combine(self.date, self.end_time)

    def __str__(self):
        return f"{self.date} {self.start_time} - {self.end_time} ({self.meeting_room} - {self.team})"


class MeetingRoomRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meeting_room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        ratings = MeetingRoomRating.objects.filter(meeting_room=self.meeting_room)
        total_score = sum(rating.score for rating in ratings)
        num_ratings = len(ratings)
        if num_ratings > 0:
            average = total_score / num_ratings
        else:
            average = 0
        return average

    def can_add_comment(self):
        if self.created_at:
            return (
                        timezone.now() - self.created_at).total_seconds() / 3600 < 24 and self.meeting_room.sessions_set.filter(
                end_time__lte=timezone.now()).exists()
        return False
