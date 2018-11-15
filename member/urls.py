# from django.urls import path
from django.conf.urls import url , include
from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/post/<int:pk>/delete/',views.DeletePost.as_view(), name='delete_post'),
    path('player/<int:pk>/',views.Player.as_view(),name='player'),
    path('player/<int:pk>/follow/',views.Following.as_view(),name='following'),
    # url(r'^$',views.index,name='index'),
    # url(r'^login$',views.login,name='login'),
    # url(r'^signup$',views.signup,name='signup'),
    path('profile/',views.Profile.as_view(),name='profile'),
    # path('home/',views.signup),
    # path('<code_name>/',views.profile)
]