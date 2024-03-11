from django.forms import forms

from rooms.models import MeetingRoomRating
class MeetingRoomRatingForm(forms.Form):
    class Meta:
        model = MeetingRoomRating
        fields = ('user','meeting_room', 'score','comment')