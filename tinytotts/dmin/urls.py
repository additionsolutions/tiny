from django.conf.urls import patterns, url
from dmin import views

urlpatterns = patterns('',
        url(r'^dmin/$', views.basic, name='basic'),
        url(r'^dmin/user$', views.UserListView.as_view(), name='userlist'),
        )