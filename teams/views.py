from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def show_teams(request):
    teams = Team.objects.all()

    return render(request, 'teams.html', {'teams': teams})

def show_team_members(request, team_id):
    if request.method == 'GET':
        team = get_object_or_404(Team, id=team_id)
        members = team.customuser_set.all()

        return render(request, 'team_members.html', {'members': members})

def delete_team(request, team_id):
    if request.method == 'GET':
        team = get_object_or_404(Team, id=team_id)
        team.delete()

        return redirect('teams:show_teams')

def create_team(request):
    if request.method == 'GET':
        form = CreateTeamForm()

        return render(request, 'create_team.html', {'form': form})
    else:
        form = CreateTeamForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('teams:show_teams')
        else:

            return render(request, 'create_team.html', {'form': form})

def show_team_reservations(request, team_id):
    if request.method == 'GET':
        team = get_object_or_404(Team, id=team_id)
        reservations = team.reservation_set.all()

        return render(request, 'reservations.html', {'reservations': reservations})