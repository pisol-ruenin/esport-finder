from django import forms
from django.contrib.auth.models import User
from .models import Team,TeamMember,TeamRole

class CreateTeamForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}))
    class Meta:
        model = Team
        fields = [
            'name',
            'email',
            'website',
            'description',
            'game',
        ]
    def save(self,commit=True):
        team = super(CreateTeamForm, self).save(commit=False)   
        team.name = self.cleaned_data['name']
        team.email = self.cleaned_data['email']
        team.website = self.cleaned_data['website']
        team.description = self.cleaned_data['description']
        team.game = self.cleaned_data['game']
        if commit:
            team.save()
            join_team = TeamMember()
            join_team.member = team.founder
            join_team.team = team
            role = TeamRole.objects.get(name="Player")
            join_team.role = role
            join_team.save()
        
        return team

class EditTeamInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}))
    class Meta:
        model = Team
        fields = [
            'name',
            'email',
            'website',
            'description',
            'game',
            'img'
        ]
