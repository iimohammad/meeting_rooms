from django import forms
from .models import *


class CreateTeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data['name']
        is_valid = name.istitle()

        if not is_valid:
            message = "You have not entered a valid name! Please try again."
            raise forms.ValidationError(message)
        
        return name

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['user', 'team']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'members']
