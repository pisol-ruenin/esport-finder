from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Post

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
    def save(self,commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user_profile = UserProfile()
        user_profile.user = user
        user_profile.pk = user.pk
        if commit:
            user.save()
            user_profile.save()
        
        return user

class ProfileForm(forms.ModelForm):
    # birtdate = forms.DateField()
    class Meta:
        model = UserProfile
        fields = [
            'codename',
            'birtdate',
            'tel',
            'streaming',
            'province',
            'game',
            'role',
            'rank',
            'profile_img',
            'cover_img'
        ]
        widgets = {
            'birtdate': forms.DateInput(attrs={'type': 'date'}),
        }
        # widget = {'birtdate':forms.DateInput(attrs={'class':'datepicker'})}


class PostStatus(forms.ModelForm):
    msg = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['msg']
    # def save(self,commit=True):
    #     post = Post()
    #     post.poster = self.request.user
    #     post.
    #     if commit:
    #         post.save()