from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import FootballClubs, Players
from .forms import PlayerForm
import json

def index(request):
    all_clubname = FootballClubs.objects.all()

    return render(request, 'teams/index.html', {'all_clubname' : all_clubname})
  # player = Players()
        # player.player_name = "blah"
        #
        # player.create()
def detail(request, id ):
    team = get_object_or_404(FootballClubs, pk=id)
    return render(request, 'teams/detail.html', {'team': team})

def player_create(request, id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlayerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data # The form gets the form results with the HTML; cleaned_data extracts the values
            team = FootballClubs.objects.get(pk=id) #retrieve the team based on our id

            # insert a new player into the team
            team.players_set.create(player_name=data['player_name'], player_position=data['player_position'])
            team.save()

            return HttpResponseRedirect('/teams/' + str(id))
    else:
        form = PlayerForm()

    return render(request, 'players/create.html', {'form': form})