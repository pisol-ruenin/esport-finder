from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from member.forms import RegistrationForm

# Create your views here.


class SignUp(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'member/signup.html'


def profile(request):
    return render(request, 'member/profile.html')

def home(request):
    return render(request, 'member/home.html')
