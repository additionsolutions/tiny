from django.conf.urls import patterns, url
from base import views
from base.views import UserListView

urlpatterns = patterns('',
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^index/', views.index, name='index'),
        url(r'^profile/$', views.profile, name='profile'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^users/$', UserListView.as_view(), name='user-list'),
        url(r'^$', views.index, name='index'),
        )