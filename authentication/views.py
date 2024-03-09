from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from authentication.forms import UserCreateForm

class CustomLoginView(LoginView):
    template_name = 'login.html'


class SignupView(CreateView):
    form_class = UserCreateForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login_view')