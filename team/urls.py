from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    # path('signup/', views.SignUp.as_view(), name='signup'),
    # url(r'^$',views.index,name='index'),
    # url(r'^login$',views.login,name='login'),
    # url(r'^signup$',views.signup,name='signup'),
    url(r'^teami$', views.teami, name='teami'),
    url(r'^team_info$', views.team_info, name='team_info'),
    url(r'^team_create$', views.team_create, name='team_create'),
    url(r'^team_manage$', views.team_manage, name='team_manage'),
    url(r'^team_editinfo$', views.team_editinfo, name='team_editinfo'),
    # url(r'^profile$',views.profile,name='profile'),
    # path('home/',views.signup),
    # path('<code_name>/',views.profile)
]
