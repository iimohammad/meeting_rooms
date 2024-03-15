from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser


class UserCreateForm(UserCreationForm):
    phone = forms.CharField(max_length=11)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'password1', 'password2', 'CompanyManager', 'phone', 'profile_image')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone']