from django.urls import path 
from authentication.views import CustomLoginView , SignupView

urlpatterns = [
    path('login/', CustomLoginView.as_view() , name='login_view'),
    path('signup/', SignupView.as_view(),name='signup_view'),
    # path('logout/', ),
    # path('profile/', ),
    # path('editprofile/', ),
    
]
