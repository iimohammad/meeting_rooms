from django.http import HttpResponseForbidden

from django.http import HttpResponseForbidden
from company.models import Manager

def manager_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                manager = Manager.objects.get(user=request.user)
                if manager.access:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponseForbidden("You do not have permission to access this page.")
            except Manager.DoesNotExist:
                return HttpResponseForbidden("You are not a manager.")
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")
    return wrapper


