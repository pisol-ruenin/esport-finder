from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'member/index.html')


def login(request):
    return render(request, 'member/login.html')

def signup(request):
    return render(request, 'member/signup.html')

def home(request):
    return render(request, 'member/home.html')

def profile(request):
    return render(request, 'member/profile.html')
