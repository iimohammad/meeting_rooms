from django.urls import path
from .views import *

app_name = 'company'

urlpatterns = [
    path('show_teams/', show_teams, name='show_teams'),
    path('show_team_members/<int:team_id>/', show_team_members, name='show_team_members'),
    path('delete_team/<int:team_id>/', delete_team, name='delete_team'),
    path('create_team/', create_team, name='create_team'),
    path('show_team_reservations/<int:team_id>/', show_team_reservations, name='show_team_reservations'),
    # path('edit_members_of_team/<int:team_id>/', TeamUpdateView.as_view(), name= 'edit_members_of_team'),
    # path('change_manager_of_team/<int:team_id>/', TeamManagerUpdateView.as_view(), name='change_manager_of_team'),
]
