from django.http import Http404
from django.shortcuts import render
from .models import FootballClubs

def index(request):
    all_clubname = FootballClubs.objects.all()

    return render(request, 'teams/index.html', {'all_clubname' : all_clubname})

def detail(request, id ):
    try:
        team = FootballClubs.objects.get(pk=id)
    except FootballClubs.DoesNotExist:
        raise Http404("Team does not exist")
    return render(request, 'teams/detail.html', {'team': team})
