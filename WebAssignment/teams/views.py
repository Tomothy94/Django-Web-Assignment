from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> This is the team homepage </h1>")

def detail(request, team_ID ):
    return HttpResponse("<h2>Details for team IDS" + str(team_ID) + "</h2>")