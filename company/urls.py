from django.urls import path
from .views import *

urlpatterns = [
    path('create_company', CompanyCreateView.as_view(), name='create_company'),
    path('update_team/<int:team_id>/', TeamUpdateView.as_view(), name='update_team'),
    path('create_team/', TeamCreateView.as_view(), name='create_team'),
    path('team_list/<int:company_id>/', TeamListView.as_view(), name='team-list'),
    path('delete/<int:pk>/', TeamDeleteView.as_view(), name='delete-team'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('delete/<int:team_id>/', TeamDeleteView.as_view(), name='delete-team'),
]
