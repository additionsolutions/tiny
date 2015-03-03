from django.conf.urls import patterns, url
from contents import views

urlpatterns = patterns('',
        #url(r'^academicduration/$', views.academicduration, name='academicduration'),
        url(r'^add_contenttype/$', views.add_contenttype, name='add_contenttype'),
        #url(r'^type/$', views.contentstype, name='contentstype'),
        #url(r'^contents/$', views.contents, name='contents'),
        #url(r'^permissions/$', views.permissions, name='permissions'),
        )