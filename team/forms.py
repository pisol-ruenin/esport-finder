from django import forms
from django.contrib.auth.models import User
from .models import Team

class CreateTeamForm(forms.ModelForm):
    email = forms.EmailField(required=True)

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
        
        return team
