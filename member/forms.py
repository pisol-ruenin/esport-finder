from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Post, Mail

class MailForm(forms.ModelForm):
    to = forms.CharField(max_length =300)
    msg = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}))      
    reciever = forms.HiddenInput()
    class Meta:
        model = Mail
        fields = ['to','topic','msg']
        widgets = {
                'reciever': forms.HiddenInput(),
            }
        labels = {
           'to': 'Message to',
        }

    def save(self,commit=True):
        mail = super(MailForm, self).save(commit=False)
        user = User.objects.get(username=self.cleaned_data.get('to'))
        mail.reciever = user
        mail.msg = self.cleaned_data['msg']
        if commit:
            mail.save()
        return mail

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
        help_texts={
            'username':'150 characters or fewer. Letters, digits and @/./+/-/_ only.',
            'password1':'Your password can\'t be too similar to your other personal information.<br>Your password must contain at least 8 characters.<br>Your password can\'t be a commonly used password.<br>Your password can\'t be entirely numeric.'
        }
    def save(self,commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username'].lower()
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