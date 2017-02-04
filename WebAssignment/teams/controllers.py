from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import FootballClubs, Players
from .forms import PlayerForm
#Controller

def index(request):
    all_clubname = FootballClubs.objects.all()

    return render(request, 'teams/index.html', {'all_clubname' : all_clubname}) #all_clubname is the model here
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

    return render(request, 'players/create.html', {'form': form}) #form is the model here

def player_edit(request, id, playerid):
    # if this is a POST request we need to process the form data
    team = FootballClubs.objects.get(pk=id) #retrieve the team based on our id
    player = team.players_set.get(pk=playerid)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlayerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data # The form gets the form results with the HTML; cleaned_data extracts the values

            # insert a new player into the team
            player.player_name=data['player_name']
            player.player_position=data['player_position']
            player.save()

            return HttpResponseRedirect('/teams/' + str(id))
    else:        
        form = PlayerForm(initial={'player_name':player.player_name, 'player_position': player.player_position})

    return render(request, 'players/edit.html', {'form': form, 'player': player})

def player_delete(request, id, playerid):
    # if this is a POST request we need to process the form data
    team = FootballClubs.objects.get(pk=id) #retrieve the team based on our id
    player = team.players_set.get(pk=playerid)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        player.delete()
        return HttpResponseRedirect('/teams/' + str(id))
    else:
        form = PlayerForm(initial={'player_name':player.player_name, 'player_position': player.player_position})

    return render(request, 'players/delete.html', {'form': form, 'player': player})

