from django.shortcuts import get_object_or_404, render
from .models import Team
# Create your views here.
def home(request):
    teams = Team.objects
    return render(request, 'home.html', {'teams' : teams})

def detail(request, team_id):
    team_detail = get_object_or_404(Team, pk = team_id)
    return render(request, 'detail.html', {'team' : team_detail})
    