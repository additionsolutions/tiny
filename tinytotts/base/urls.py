from django.conf.urls import patterns, url
from base import views

urlpatterns = patterns('',
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^index/', views.index, name='index'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^$', views.index, name='index'),
        )