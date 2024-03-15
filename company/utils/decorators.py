from django.http import HttpResponseForbidden
from company.models import Team
from accounts.models import CustomUser
from django.contrib.auth.decorators import user_passes_test

def manager_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                manager = Team.objects.get(user=request.user)
                if manager.permission:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponseForbidden("You do not have permission to access this page.")
            except Team.DoesNotExist:
                return HttpResponseForbidden("You are not a manager.")
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")
    return wrapper


def check_company_manager(func):
    def wrapper(model_instance):
        if model_instance.CompanyCEO == CustomUser.readonly.CompanyCEO:
            return func(model_instance)
        else:
            raise ValueError("you are not company manager. you can't make changes")
    return wrapper




