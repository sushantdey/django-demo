from django.shortcuts import render, redirect

from main.service import team_service
from main.service.team_service import TeamForm


# Create your views here.
def create(request):
    if request.method == "POST":
        team = team_service.create(request)
        return render(request, 'team/team.html', {'team': team})
    else:
        form = TeamForm()
    return render(request, "team/create.html", {'form': form})


def get_team(request, team_id):
    return render(request, 'team/team.html', {'team': team_service.get_team(team_id)})


def get_all_teams(request):
    return render(request, 'team/teams.html', {'teams': team_service.get_all_teams()})
