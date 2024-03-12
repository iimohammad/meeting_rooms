from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

user = get_user_model()


class MeetingRoom(models.Model):
    room_name = models.CharField(max_length=20, unique=True)
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

    def __str__(self):
        return self.room_name


class Sessions(models.Model):
    name = models.CharField(max_length=30, default="session")
    team = models.ForeignKey('company.Team', on_delete=models.CASCADE)
    meeting_room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ['date', 'start_time']

    def is_past(self):
        return timezone.now() > timezone.datetime.combine(self.date, self.end_time)

    def __str__(self):
        return f"{self.date} {self.start_time} - {self.end_time} ({self.meeting_room} - {self.team})"


class MeetingRoomRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meeting_room = models.ForeignKey('MeetingRoom', on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text=_("Enter a rating between 1 and 5.")
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.meeting_room} - {self.score}"

    class Meta:
        verbose_name = _("Meeting Room Rating")
        verbose_name_plural = _("Meeting Room Ratings")

    @property
    def average_rating(self):
        return MeetingRoomRating.objects.filter(meeting_room=self.meeting_room).aggregate(models.Avg('score'))[
            'score__avg'] or 0

    @property
    def can_add_comment(self):
        return (timezone.now() - self.created_at).total_seconds() / 3600 < 24 and not self.comment


class SessionRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.ForeignKey('Sessions', on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text=_("Enter a rating between 1 and 5.")
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.session} - {self.score}"

    class Meta:
        verbose_name = _("Session Rating")
        verbose_name_plural = _("Session Ratings")

    @property
    def can_add_comment(self):
        return (timezone.now() - self.created_at).total_seconds() / 3600 < 24 and not self.comment
