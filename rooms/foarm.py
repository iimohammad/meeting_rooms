# در فایل foarm.py

from django import forms
from .models import MeetingRoom

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = MeetingRoom
        fields = ['room', 'location', 'capacity', 'available']  # یا فیلدهای دیگری که می‌خواهید در فرم نمایش داده شوند
        widgets = {
            'room': forms.TextInput(attrs={'placeholder': 'Room Name'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'capacity': forms.NumberInput(attrs={'placeholder': 'Capacity'}),
        }
