from django.shortcuts import render
from .models import Team
from .forms import TeamMembersForm

def edit_team_members(request, team_id):
    team = Team.objects.get(id=team_id)
    
    if request.method == 'POST':
        form = TeamMembersForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
    else:
        form = TeamMembersForm(instance=team)
    
    return render(request, 'edit_team_members.html', {'form': form})


