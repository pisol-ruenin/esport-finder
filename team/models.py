from django.db import models
from django.contrib.auth.models import User
from member.models import Game

class Team(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)
    description = models.CharField(max_length=100,blank=True)
    founder = models.OneToOneField(User,models.SET_NULL,blank=True,null=True)
    game = models.ForeignKey(Game,models.SET_NULL,blank=True,null=True)
    class Meta:
        unique_together = (("game", "name"))

class TeamMember(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    member = models.ForeignKey(User,on_delete=models.CASCADE)
    join_date = models.DateField(auto_now_add=True)
    class Meta:
        unique_together = (("team","member"))

