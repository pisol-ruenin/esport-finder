from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = "team"
urlpatterns = [
    # path('signup/', views.SignUp.as_view(), name='signup'),
    # url(r'^$',views.index,name='index'),
    # url(r'^login$',views.login,name='login'),
    # url(r'^signup$',views.signup,name='signup'),
    path('', views.Teami.as_view(), name='teami'),
    path('team_info/<int:pk>/', views.TeamInfo.as_view(), name='team_info'),
    url(r'^team_create$', views.CreateTeam.as_view(), name='team_create'),
    url(r'^team_manage$', views.team_manage, name='team_manage'),
    path('team_info/<int:pk>/edit_info/', views.EditInfo.as_view(), name='team_editinfo'),
    url(r'^team_list$', views.team_list, name='team_list'),
    url(r'^team_recruitment$', views.team_recruitment.as_view(), name='team_recruitment'),
    url(r'^team_recruitment_list$', views.team_recruitment_list.as_view(), name='team_recruitment_list'),
    url(r'^team_recruitment_create$', views.team_recruitment_create.as_view(), name='team_recruitment_create'),
    path('search/',views.FilterTeam.as_view(),name="team_search")
    # url(r'^profile$',views.profile,name='profile'),
    # path('home/',views.signup),
    # path('<code_name>/',views.profile)
]
