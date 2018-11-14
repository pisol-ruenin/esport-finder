from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':['input','label']}))
    username2 = forms.CharField(widget=forms.TextInput(attrs={'class':['input','label']}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':['input','label']}))