from django.urls import path
from main.controller import team_controller


urlpatterns = [
    path('create', team_controller.create, name='create_team'),
    path('<int:team_id>', team_controller.get_team, name='get_team'),
    path('', team_controller.get_all_teams, name='get_all_teams')
]
