from django.urls import path
from .views import *

urlpatterns = [
    path('create_team/', TeamCreateView.as_view(), name='create-team'),
    path('delete_team/<int:pk>/', TeamDeleteView.as_view(), name='delete-team'),
    path('update_team/<int:pk>/', TeamUpdateView.as_view(), name='update-team'),
    path('team_list/<int:company_id>/', TeamListView.as_view(), name='team-list'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    # path('team_members/<int:pk>/', TeamMembersListView.as_view(), name='team-members'),
    # path('delete_member/<int:team_id>/<int:member_id>/', MemberDeleteView.as_view(), name='delete-member'),
    path('team_sessions/<int:pk>/', TeamSessionsView.as_view(), name='team-sessions'),
    path('create_company/', CompanyCreateView.as_view(), name='create-company'),
    path('update_company/<int:pk>/', CompanyUpdateView.as_view(), name='update-company'),
    path('delete_company/<int:pk>/', CompanyDeleteView.as_view(), name='delete-company'),
    path('company_list/', CompanyListView.as_view(), name='company-list'),
]
