# from django.urls import path
from django.conf.urls import url , include
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    # url(r'^$',views.index,name='index'),
    # url(r'^login$',views.login,name='login'),
    # url(r'^signup$',views.signup,name='signup'),
    # url(r'^home$',views.home,name='home'),
    url(r'^profile$',views.profile,name='profile'),
    # path('home/',views.signup),
    # path('<code_name>/',views.profile)
]