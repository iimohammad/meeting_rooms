from django import forms
from django.contrib.auth.forms import UserCreationForm
from customuser.models import CustomUser

class UserCreateForm(UserCreationForm):
    phone = forms.CharField(max_length=11)
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'phone')
