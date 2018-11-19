from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Team,TeamMember,TeamRole
from team.forms import CreateTeamForm,EditTeamInfoForm
from django.http import HttpResponseRedirect
from .filters import TeamFilter
from team.forms import TeamRecruitForm
from team.models import TeamRecruitPost

class Teami(generic.View):
    template_name = 'team/teami.html'
    # def get_context_data(self,*atg,**kwargs):
    #     context['ck_founder'] = len(Team.objects.filter(founder=self.request.user))
    #     return context
    def dispatch(self,*args,**kwargs):
        member = TeamMember.objects.get(member=self.request.user)
        if member:
            return HttpResponseRedirect(reverse_lazy('team:team_info',kwargs={'pk': member.team.pk}))
        return super(Teami, self).dispatch(*args, **kwargs)

class CreateTeam(generic.CreateView):
    form_class = CreateTeamForm
    template_name = 'team/team_create.html'
    model=Team

    def get_success_url(self, *arg, **kwargs):
        team = Team.objects.get(founder=self.request.user)
        return reverse_lazy('team:team_info',kwargs={'pk': team.pk})

    def form_valid(self, form):
        user = self.request.user
        form.instance.founder = user
        return super(CreateTeam, self).form_valid(form)

class TeamInfo(generic.DetailView):
    template_name = 'team/team_info.html'
    model = Team

    def get_context_data(self, **kwargs):
        context = super(TeamInfo,self).get_context_data(**kwargs)
        context['team'] = Team.objects.get(pk=self.kwargs['pk'])
        context['team_member'] = TeamMember.objects.filter(team=context['team'],role=1)
        context['team_manager'] = TeamMember.objects.filter(team=context['team'],role=2)
        context['ck_founder'] = len(Team.objects.filter(founder=self.request.user,pk=self.kwargs['pk']))
        print(context['team_member'])
        return context

class EditInfo(generic.UpdateView):
    model = Team
    template_name = 'team/team_editinfo.html'
    form_class = EditTeamInfoForm

    def get_success_url(self, *arg, **kwargs):
        team = Team.objects.get(founder=self.request.user)
        return reverse_lazy('team:team_info',kwargs={'pk': team.pk})

class FilterTeam(generic.ListView):
    model = Team
    template_name = 'team/team_list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TeamFilter(self.request.GET,queryset=self.get_queryset())
        return context

def team_manage(request):
    return render(request, 'team/team_manage.html')

def team_list(request):
    return render(request, 'team/team_list.html')

class team_recruitment(generic.CreateView):
    template_name = 'team/team_recruitment.html'
    context_object_name = "feed"
    # def get(self,request):
    #     posts = TeamRecruitPost.objects.all()
    #     args = {'posts':posts}
    #     return render(request,self.template_name,args)

class team_recruitment_list(generic.ListView):
    template_name = 'team/team_recruitment_list.html'
    def get(self,request):
        posts = TeamRecruitPost.objects.all()
        
        args = {'posts':posts}
        return render(request,self.template_name,args)

class team_recruitment_create(generic.CreateView):
    template_name =  'team/team_recruitment_create.html'
    success_url = reverse_lazy('team:team_recruitment_list')
    form_class = TeamRecruitForm
