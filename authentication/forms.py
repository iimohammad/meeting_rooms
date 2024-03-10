from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import CustomUser


class UserCreateForm(UserCreationForm):
    phone = forms.CharField(max_length=11)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'password1', 'password2', 'phone', 'profile_image')
