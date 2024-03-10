from django import forms
from .models import Team

class TeamMembersForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['members']  
