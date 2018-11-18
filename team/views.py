from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from member.forms import RegistrationForm


def teami(request):
    return render(request, 'team/teami.html')


def team_info(request):
    return render(request, 'team/team_info.html')


def team_create(request):
    return render(request, 'team/team_create.html')


def team_manage(request):
    return render(request, 'team/team_manage.html')

def team_editinfo(request):
    return render(request, 'team/team_editinfo.html')

def team_list(request):
    return render(request, 'team/team_list.html')

def team_recruitment(request):
    return render(request, 'team/team_recruitment.html')

def team_recruitment_create(request):
    return render(request, 'team/team_recruitment_create.html')