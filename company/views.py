from django.shortcuts import render, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView, View
from .models import Team, Company
from django.utils.decorators import method_decorator


# Team Views
@method_decorator(login_required, name='dispatch')
class TeamCreateView(CreateView):
    model = Team
    fields = ['company', 'name', 'manager', 'members']
    template_name = 'create_team.html'

    def get_success_url(self):
        company_id = self.object.company.id
        return reverse_lazy('team-list', kwargs={'company_id': company_id})


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
    template_name = 'update_team.html'
    
    def get_success_url(self):
        company_id = self.object.company.id
        return reverse_lazy('team-list', kwargs={'company_id': company_id})



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


""" class TeamMembersListView(LoginRequiredMixin, ListView):
    model = Team
    template_name = 'team_members.html'
    context_object_name = 'members'

    def get_queryset(self):
        team_id = self.kwargs.get('pk')
        team = get_object_or_404(Team, id=team_id)
        return team.members.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_id = self.kwargs.get('pk')
        team = get_object_or_404(Team, id=team_id)
        context['team'] = team
        return context """


""" class MemberDeleteView(View):
    template_name = 'member_delete.html'

    def get(self, request, team_id, member_id):
        team = get_object_or_404(Team, id=team_id)
        member = get_object_or_404(CustomUser, id=member_id)
        team.members.remove(member)
        messages.success(request, f"{member} has been removed from {team.name}.")

        return redirect('team-members', pk=team.id) """


class TeamSessionsView(View):
    template_name = 'sessions.html'

    def get(self, request, pk):
        team = get_object_or_404(Team, id=pk)
        sessions = team.sessions.all()
        return render(request, self.template_name, {'sessions': sessions, 'team': team})


# Company Views
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
