from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('team/<int:team_id>/edit/', views.edit_team_members, name='edit_team_members'),
]

