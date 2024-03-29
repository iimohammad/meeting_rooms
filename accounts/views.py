from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import UserCreateForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .models import CustomUser
from .forms import EditProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from notification.utils import *
user = get_user_model


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('profile_view')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class EmailLoginView(View):

    def get(self, request):
        return render(request, 'emaillogin.html', context={'otp': 0})

    @method_decorator(csrf_exempt)
    def post(self, request):
        return render(request, 'emaillogin.html', context={'otp': 1})


class SignupView(CreateView):
    form_class = UserCreateForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login_view')

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        response = super().form_valid(form)

        user = form.instance
        send_sign_up_notification(user.email)
        return response


@login_required
def profile_view(request):
    print("--------------------")
    # print(request.user.username)
    profile = request.user
    # print(profile.username)
    context = {
        'profile': {
            'User Name': profile.username,
            'First Name': profile.first_name,
            'Last Name': profile.last_name,
            'Email': profile.email,
            'Phone': profile.phone,
        },
        'image': profile.profile_image,
    }
    return render(request, 'profile.html', context=context)


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = EditProfileForm
    template_name = 'editprofile.html'
    success_url = reverse_lazy('profile_view')

    def get_object(self, queryset=None):
        return self.request.user


