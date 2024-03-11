from django.urls import path
from .views import *

urlpatterns = [
    # path('show_teams/', show_teams, name='show_teams'),
    path('create_company', CompanyCreateView.as_view(), name='create_company'),
    # path('edit_members_of_team/<int:team_id>/', TeamUpdateView.as_view(), name= 'edit_members_of_team'),
    # path('change_manager_of_team/<int:team_id>/', TeamManagerUpdateView.as_view(), name='change_manager_of_team'),
    path('create_team/', TeamCreateView.as_view(), name='create_team'),
    path('team_list/<int:company_id>/', TeamListView.as_view(), name='team-list'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),

]
