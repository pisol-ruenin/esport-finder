from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from member.forms import RegistrationForm,PostStatus
from .models import UserProfile,Post,Follow
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models.expressions import RawSQL
# Create your views here.


class SignUp(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'member/signup.html'

class Profile(generic.CreateView,LoginRequiredMixin,generic.ListView):
    form_class = PostStatus
    raise_exception = True
    context_object_name = "post_list"
    template_name = 'member/profile.html'
    success_url = reverse_lazy('member:profile')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = User
    
    def get_context_data(self, **kwargs):
        context = super(Profile,self).get_context_data(**kwargs)
        # context['player'] = User.objects.get(pk=self.kwargs['pk'])
        context['post_list'] = Post.objects.filter(poster=self.request.user.pk)
        context['follower'] = len(Follow.objects.filter(following=self.request.user.pk))
        context['following'] = len(Follow.objects.filter(follower=self.request.user.pk))
        return context

    def get_queryset(self):
        post = Post.objects.filter(poster=self.request.user)[::-1]
        return post

    def form_valid(self, form):
        user = self.request.user
        form.instance.poster = user
        return super(Profile, self).form_valid(form)

class DeletePost(generic.DeleteView,LoginRequiredMixin):
    raise_exception = True
    model = Post
    success_url = reverse_lazy('member:profile')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get(self, *args, **kwargs):
        """
        This has been overriden because by default
        DeleteView doesn't work with GET requests
        """
        return self.delete(*args, **kwargs)

class Player(generic.DetailView):
    template_name = 'member/player.html'
    model = User
    def get_context_data(self, **kwargs):
        context = super(Player,self).get_context_data(**kwargs)
        # context['player'] = User.objects.get(pk=self.kwargs['pk'])
        context['post_list'] = Post.objects.filter(poster=self.get_object())
        context['follower'] = len(Follow.objects.filter(following=self.get_object()))
        context['following'] = len(Follow.objects.filter(follower=self.get_object()))
        return context
    # def get_queryset(self):
    #     player = User.objects.get(pk=self.kwargs['pk'])
    #     return player
    def dispatch(self,*args, **kwargs):
        if self.request.user.pk==self.kwargs['pk']:
            return redirect('member:profile')
        return super(Player, self).dispatch(*args, **kwargs)

class Following(generic.CreateView):
    model = Follow
    def dispatch(self,*args, **kwargs):
        follow = Follow()
        follower = User.objects.get(pk=self.request.user.pk)
        following = User.objects.get(pk=self.kwargs['pk'])
        follow.follower = follower
        follow.following = following
        follow.save()
        return redirect('member:player', kwargs={'pk': self.kwargs['pk']})
        

class Home(generic.ListView):
    template_name='member/home.html'
    context_object_name = "feed"
    def get_queryset(self):
        following = Follow.objects.filter(follower=self.request.user.pk)
        feed = list()
        for i in following:
            feed.append(Post.objects.filter(poster=i.pk))
        return feed[::-1]
