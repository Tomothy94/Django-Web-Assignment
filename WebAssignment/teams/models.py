#DAL
from django.db import models


#Team ID and Team Name
# Create your models here.

class FootballClubs(models.Model):
    clubname = models.CharField(max_length =250)
    teamID = models.CharField(max_length=10)


    def __str__(self):
        return self.clubname + ' - ' + str(self.id)
    # str casts .id function to string as it is inbuilt as an int

class Players(models.Model):
    footballClubs = models.ForeignKey(FootballClubs, on_delete=models.CASCADE)
    player_position = models.CharField(max_length=20)
    player_name = models.CharField(max_length=250)

    # def create(self):
    #     models.create(self)
    #     models.save()

    # def get(self, id):
    #     return self.get(id);
    #
    # def delete(self, id):
    #     self.delete(id)
    #     self.save()

    def __str__(self):
        return self.player_name
