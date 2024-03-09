from django import forms
from .models import *


class CreateTeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = "__all__"

    def clean_manager(self):
        manager = self.cleaned_data['manager']
        is_valid = manager.member_of is None

        if not is_valid:
            message = "The user you have chosen as your team manager is already in another team!\
                       Please choose a user who doesn't have a team."
            raise forms.ValidationError(message)
        return manager
