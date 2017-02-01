from django.http import HttpResponse
from django.template import loader
from .models import FootballClubs

def index(request):
    all_clubname = FootballClubs.objects.all()
    template = loader.get_template('teams/index.html')
    context = {
        'all_clubname' : all_clubname,
    }

    return HttpResponse(template.render(context, request))

def detail(request, teamID ):
    return HttpResponse("<h2>Details for team IDS" + str(teamID) + "</h2>")