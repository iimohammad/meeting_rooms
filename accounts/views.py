from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import UserCreateForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
user = get_user_model()


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_to = 'profile_view'


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


def profile_view(request):
    # profile = user.objects.get(user=request.user)[0]
    profile = user.objects.get(pk=1)
    context = {
        'profile': {'User Name': profile.get_username(),
                    'First Name': profile.first_name,
                    'Last Name': profile.last_name,
                    'Email': profile.email,
                    'Phone': profile.phone,
                    },
        'image': profile.profile_image,
    }
    return render(request, 'profile.html', context=context)


# class PostEditView(UpdateView):
#     model = user
#     template_name = 'editprofile.html'
#     fields = ['username', 'email', 'first_name', 'last_name',
#               'password1', 'password2', 'phone', 'profile_image']
    # pk_url_kwarg = 'pk'


def edit_profile_view(request):
    # profile = user.objects.get(user=request.user)[0]
    profile = user.objects.get(pk=1)
    profile = {
        'username': profile.get_username(),
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'email': profile.email,
        'phone': profile.phone,
        'profile_image': profile.profile_image,
    }
    context = {'profile': profile}
    return render(request, 'editprofile.html', context)
