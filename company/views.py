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
    fields = ['company', 'name', 'manager', 'members']
    template_name = 'team_update.html'

    def get_success_url(self):
        return reverse_lazy('team-detail', kwargs={'pk': self.object.pk})


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


class TeamMemberListView(DetailView):
    model = Team
    template_name = 'team_member_list.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = self.get_object()
        members = team.members.all()
        context['members'] = members
        return context
