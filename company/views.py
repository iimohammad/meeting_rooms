from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from .models import Team, Company
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


# Team Views
@method_decorator(login_required, name='dispatch')
class TeamCreateView(CreateView):
    model = Team
    fields = ['company', 'name', 'manager', 'members']
    template_name = 'team_create.html'
    success_url = reverse_lazy('home:home')


@method_decorator(login_required, name='dispatch')
class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'team_confirm_delete.html'

    def get_success_url(self):
        company_id = self.object.company.id
        return reverse_lazy('team-list', kwargs={'company_id': company_id})


@method_decorator(login_required, name='dispatch')
class TeamUpdateView(UpdateView):
    model = Team
    fields = ['company', 'name', 'manager']
    template_name = 'team_update.html'
    success_url = reverse_lazy('team-list')


@method_decorator(login_required, name='dispatch')
class TeamListView(ListView):
    model = Team
    template_name = 'team_lists.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return Team.objects.filter(company_id=self.kwargs['company_id'])


class TeamDetailView(DetailView):
    model = Team
    template_name = 'team_detail.html'


class TeamMembersListView(LoginRequiredMixin, ListView):
    model = Team
    template_name = 'team_members.html'
    context_object_name = 'members'

    def get_queryset(self):
        team_id = self.kwargs.get('team_id')
        team = get_object_or_404(Team, id=team_id)
        return team.customuser_set.all()


# Company Views
class CompanyCreateView(CreateView):
    model = Company
    fields = ['name', 'phone', 'address']
    template_name = 'company_create.html'
    # success_url = reverse_lazy('company-list')


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
