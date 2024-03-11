from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# from utils.decorators import *
from django.views.generic import UpdateView
from django.urls import reverse_lazy

@login_required
def show_teams(request):
    teams = Team.objects.all()

    return render(request, 'teams.html', {'teams': teams})

@login_required
def show_team_members(request, team_id):
    if request.method == 'GET':
        team = get_object_or_404(Team, id=team_id)
        members = team.customuser_set.all()

        return render(request, 'team_members.html', {'members': members})

@login_required
def delete_team(request, team_id):
    if request.method == 'GET':
        team = get_object_or_404(Team, id=team_id)
        team.delete()

        return redirect('teams:show_teams')

@login_required
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

@login_required
def show_team_reservations(request, team_id):
    if request.method == 'GET':
        team = get_object_or_404(Team, id=team_id)
        reservations = team.reservation_set.all()

        return render(request, 'reservations.html', {'reservations': reservations})


@login_required
class TeamManagerUpdateView(UpdateView):
    model = Manager
    form_class = ManagerForm
    fields = ['user']
    template_name = 'update_manager.html'
    success_url = reverse_lazy('show_team_members')

    def get_object(self, queryset=None):
        team_id = self.kwargs.get('team_id')
        team_manager = get_object_or_404(Manager, user=self.request.user, team_id=team_id)
        return team_manager

# @login_required
# @manager_required
# class TeamUpdateView(UpdateView):
#     model = Team
#     form_class = TeamForm
#     template_name = 'update_team.html'
#     success_url = reverse_lazy('show_team_members')
#
#     def get_object(self, queryset=None):
#         team_id = self.kwargs.get('team_id')
#         team = get_object_or_404(Team, id=team_id)
#         return team

