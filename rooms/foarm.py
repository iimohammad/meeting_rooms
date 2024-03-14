from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ReserveMeetingRoomForm(forms.ModelForm):
    class Meta:
        model = Sessions
        fields = ['team', 'meeting_room', 'date', 'start_time', 'end_time']

    def clean(self):
        cleaned_data = super().clean()
        meeting_room = cleaned_data.get('meeting_room')
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time:
            if start_time >= end_time:
                raise ValidationError("End time must be after start time.")

        if meeting_room and date and start_time and end_time:
            if not meeting_room.is_available(date, start_time, end_time):
                raise ValidationError("This meeting room is not available at the specified time and date.")

        return cleaned_data


class MeetingRoomRatingForm(forms.ModelForm):
    pass
