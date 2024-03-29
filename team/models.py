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
    img = models.ImageField(default='default/default_team.png',blank=True)
    class Meta:
        unique_together = (("game", "name"))

    def __str__(self):
        return self.name + " - " + self.game.name

class TeamRole(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class TeamMember(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    member = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.ForeignKey(TeamRole,models.SET_NULL,null=True)
    join_date = models.DateField(auto_now_add=True)
    class Meta:
        unique_together = (("team","member"))
    def __str__(self):
        return  self.member.username + " - " + self.team.name + " - " + self.role.name

class TeamRecruitPost(models.Model):
    # recruit_id = models.CharField(max_length=4)
    id = models.IntegerField(primary_key=True)
    heading = models.CharField(max_length=50)
    # img_cover = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add='')
    end_date = models.DateField(auto_now_add='')
    # team_name = models.CharField(max_length=20)