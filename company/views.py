from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# from utils.decorators import *
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView,ListView
from .models import Team, Company


@login_required
class TeamCreateView(CreateView):
    model = Team
    fields = ['company', 'name', 'manager']
    template_name = 'team_create.html'
    success_url = reverse_lazy('team-list')  # Redirect to team list after successful creation


@login_required
class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'team_confirm_delete.html'
    success_url = reverse_lazy('team-list')  # Redirect to team list after successful deletion


@login_required
class TeamUpdateView(UpdateView):
    model = Team
    fields = ['company', 'name', 'manager']
    template_name = 'team_update.html'
    success_url = reverse_lazy('team-list')  # Redirect to team list after successful update


@login_required
class TeamListView(ListView):
    model = Team
    template_name = 'team_list.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return Team.objects.filter(company_id=self.kwargs['company_id'])


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


# @login_required
# class TeamManagerUpdateView(UpdateView):
#     model = Manager
#     form_class = ManagerForm
#     fields = ['user']
#     template_name = 'update_manager.html'
#     success_url = reverse_lazy('show_team_members')
#
#     def get_object(self, queryset=None):
#         team_id = self.kwargs.get('team_id')
#         team_manager = get_object_or_404(Manager, user=self.request.user, team_id=team_id)
#         return team_manager


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


class CompanyCreateView(CreateView):
    model = Company
    fields = ['name', 'phone', 'address']
    template_name = 'company_create.html'
    success_url = reverse_lazy('company-list')


class CompanyUpdateView(UpdateView):
    model = Company
    fields = ['name', 'phone', 'address']
    template_name = 'company_update.html'
    success_url = reverse_lazy('company-list')


class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('company-list')
    template_name = 'company_confirm_delete.html'


class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'
    context_object_name = 'companies'