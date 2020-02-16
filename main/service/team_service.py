from django import forms
from main.models.team import Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"


def create(request):
    form = TeamForm(request.POST)
    if form.is_valid():
        try:
            return form.save()
        except:
            pass


def get_team(team_id):
    return Team.objects.get(id=team_id)


def get_all_teams():
    return Team.objects.all()