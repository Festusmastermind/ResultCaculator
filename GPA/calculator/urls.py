from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
#from .views import ResultCreateView



urlpatterns = [
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^create_acct/$', views.createAcct, name='create_acct'),
    url(r'^bio_reg/$', views.bio_reg, name='bio_reg'),
    url(r'^myprofile/$', views.myprofile, name='myprofile'),
    url(r'^add_result/$', views.add_result, name='add_result'),
    url(r'^load_result/$', views.load_result, name='load_result'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='calculator/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='calculator/logout.html'), name='logout'),

]