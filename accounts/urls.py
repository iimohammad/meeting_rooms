from django.urls import path
from accounts.views import CustomLoginView, SignupView, profile_view, edit_profile_view, EmailLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', view=CustomLoginView.as_view(), name='login_view'),
    path('emaillogin/', EmailLoginView.as_view(), name='email_login_view'),
    # path('login_phone/', CustomLoginView.as_view(), name='login_view'),
    # path('login_github/', CustomLoginView.as_view(), name='login_view'),
    # path('login_google/', CustomLoginView.as_view(), name='login_view'),
    path('signup/', SignupView.as_view(), name='signup_view'),
    path('profile/', profile_view, name='profile_view'),
    path('editprofile/', edit_profile_view),
    path('signup/', SignupView.as_view(), name='reserve_room'),
    path('logout/', LogoutView.as_view(next_page='login_view'), name='logout'),
]
