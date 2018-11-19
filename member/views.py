from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.views import generic
from member.forms import RegistrationForm, PostStatus, ProfileForm, MailForm
from .models import UserProfile,Post,Follow,Mail
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .filters import MemberFilter


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
        context['post_list'] = Post.objects.filter(poster=self.request.user.pk)
        context['follower'] = Follow.objects.filter(following=self.request.user.pk)
        context['following'] = Follow.objects.filter(follower=self.request.user.pk)
        context['follower_len'] = len(Follow.objects.filter(following=self.request.user.pk))
        context['following_len'] = len(Follow.objects.filter(follower=self.request.user.pk))
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
        context['ck_follow'] = len(Follow.objects.filter(following=self.kwargs['pk'],follower=self.request.user.pk))
        context['follower'] = Follow.objects.filter(following=self.kwargs['pk'])
        context['following'] = Follow.objects.filter(follower=self.kwargs['pk'])
        context['post_list'] = Post.objects.filter(poster=self.kwargs['pk'])
        context['follower_len'] = len(Follow.objects.filter(following=self.kwargs['pk']))
        context['following_len'] = len(Follow.objects.filter(follower=self.kwargs['pk']))
        return context
    def dispatch(self,*args, **kwargs):
        if self.request.user.pk==self.kwargs['pk']:
            return redirect('member:profile')
        return super(Player, self).dispatch(*args, **kwargs)

class Following(generic.View):
    model = Follow

    def get_success_url(self, *arg, **kwargs):
        return reverse_lazy('member:player',kwargs={'pk': self.kwargs['pk']})

    def dispatch(self,*args, **kwargs):
        follow = Follow()
        follower = User.objects.get(pk=self.request.user.pk)
        following = User.objects.get(pk=self.kwargs['pk'])
        follow.follower = follower
        follow.following = following
        follow.save()
        # reverse_lazy('member:player',kwargs={'pk': self.kwargs['pk']})
        return HttpResponseRedirect(reverse_lazy('member:player',kwargs={'pk': self.kwargs['pk']}))

class Unfollow(generic.View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get_success_url(self, *arg, **kwargs):
        return reverse_lazy('member:player', kwargs={'pk': self.kwargs['pk']})
        
    def dispatch(self,*args, **kwargs):
        unfollow = Follow.objects.filter(follower=self.request.user.pk,following=self.kwargs['pk'])
        unfollow.delete()
        return HttpResponseRedirect(reverse_lazy('member:player', kwargs={'pk': self.kwargs['pk']}))

class MailBox(generic.ListView):
    model = Mail
    template_name = 'member/mail.html'
    def get_context_data(self, **kwargs):
        context = super(MailBox,self).get_context_data(**kwargs)
        context['mail_list'] = Mail.objects.filter(reciever=self.request.user)[::-1]
        return context
    

class SendMail(generic.CreateView):
    form_class = MailForm
    model = Mail
    template_name = 'member/send_mail.html'
    success_url = reverse_lazy('member:mail')
    def get_context_data(self, **kwargs):
        context = super(SendMail,self).get_context_data(**kwargs)
        context['reciever'] =  self.request.POST.get("reciever","")
        return context
    def form_valid(self, form):
        user = User.objects.get(pk=self.request.user.pk)
        form.instance.sender = user
        return super(SendMail, self).form_valid(form)

class Home(generic.ListView):
    template_name='member/home.html'
    context_object_name = "feed"
    def get_queryset(self):
        following = Follow.objects.filter(follower=self.request.user.pk)
        print(following)
        feed = Follow.objects.none()
        for i in following:
            temp = Post.objects.filter(poster=i.following.id)
            feed = feed | temp
        return feed.distinct().order_by('datetime')[::-1]

class EditProfile(generic.UpdateView):
    template_name = 'member/edit_profile.html'
    raise_exception = True
    model = UserProfile
    form_class = ProfileForm
    # fields = ['codename','birtdate','tel','streaming','province','game','role','rank','profile_img','cover_img']

    def get_success_url(self, *arg, **kwargs):
        return reverse('member:profile')

    def dispatch(self, *args, **kwargs):
        # user_profile = UserProfile.objects.get(pk=self.request.user.pk)
        if self.request.user.pk != self.kwargs['pk']:
            return redirect('member:profile')
        return super(EditProfile, self).dispatch(*args, **kwargs)


class MailDetail(generic.DetailView):
    template_name = 'member/mail_detail.html'
    model = Mail
    def get_context_data(self, **kwargs):
        context = super(MailDetail,self).get_context_data(**kwargs)
        context['mail_detail'] = Mail.objects.get(pk=self.kwargs['pk'])
        return context
    def dispatch(self,*args,**kwargs):
        mail = Mail.objects.get(pk=self.kwargs['pk'])
        if self.request.user.pk!=mail.reciever.pk:
            return redirect('member:mail')

        return super(MailDetail, self).dispatch(*args, **kwargs)

class DeleteMail(generic.DeleteView):
    raise_exception = True
    model = Mail
    success_url = reverse_lazy('member:mail')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class FilterUser(generic.ListView):
    model = UserProfile
    template_name = 'member/search_user.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MemberFilter(self.request.GET,queryset=self.get_queryset())
        return context

