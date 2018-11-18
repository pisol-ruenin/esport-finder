from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    genre = models.CharField(max_length=20)
    img = models.ImageField(blank=True)
    def __str__(self):
        return self.name

class Country(models.Model):
    province = models.CharField(max_length=10,primary_key=True)
    counrty = models.CharField(max_length=10)
    def __str__(self):
        return self.province

class Role(models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    duty = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class GameRole(models.Model):
    game_name = models.ForeignKey(Game,on_delete=models.CASCADE)
    role_name = models.ForeignKey(Role,on_delete=models.CASCADE)
    class Meta:
        unique_together = (("game_name","role_name"))

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    codename = models.CharField(max_length=10,blank=True)
    streaming = models.CharField(max_length=30,blank=True)
    tel = models.CharField(max_length=10,blank=True)
    province = models.ForeignKey(Country,models.SET_NULL,blank=True,null=True)
    rank = models.CharField(max_length=30,blank=True)
    game = models.ForeignKey(Game,models.SET_NULL,blank=True,null=True)
    role = models.ForeignKey(Role,models.SET_NULL,blank=True,null=True)
    birtdate = models.DateField(null=True)
    profile_img = models.ImageField(default='default/default_profile.png',blank=True)
    cover_img = models.ImageField(default='default/default_cover.png', blank=True)
    

class Post(models.Model):
    poster = models.ForeignKey(User,on_delete=models.CASCADE)
    msg = models.CharField(max_length=1000)
    datetime = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (("poster","datetime"))
    
class Mail(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_requests_sender')
    reciever = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_requests_reciever')
    topic = models.CharField(max_length=50)
    msg = models.CharField(max_length=300)
    datetime = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (("sender", "reciever","datetime"))

class Follow(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_requests_follower')
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_requests_followed')
    date = models.DateField(auto_now_add=True)
    class Meta:
        unique_together = (("follower", "following"))
