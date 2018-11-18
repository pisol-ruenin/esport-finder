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
    path('player/<int:pk>/unfollow/',views.Unfollow.as_view(),name='unfollow'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('profile/<int:pk>/edit/',views.EditProfile.as_view(),name='edit_profile'),
    path('mail/',views.MailBox.as_view(),name='mail'),
    path('mail/send/',views.SendMail.as_view(),name='send_mail'),
    path('mail/<int:pk>/',views.MailDetail.as_view(),name='mail_detail'),
    path('mail/<int:pk>/delete/',views.DeleteMail.as_view(),name='delete_mail')
]