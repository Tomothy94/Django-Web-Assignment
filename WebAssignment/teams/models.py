from django.db import models


#Team ID and Team Name
# Create your models here.

class FootballClubs(models.Model):
    clubname = models.CharField(max_length =250)
    teamID = models.CharField(max_length=10)


    def __str__(self):
        return self.clubname + ' - ' + self.teamID

class Players(models.Model):
    footballClubs = models.ForeignKey(FootballClubs, on_delete=models.CASCADE)
    player_position = models.CharField(max_length=20)
    player_name = models.CharField(max_length=250)


    def __str__(self):
        return self.player_name
