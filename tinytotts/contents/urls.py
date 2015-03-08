from django.conf.urls import patterns, url
from contents import views

urlpatterns = patterns('',
        #url(r'^academicduration/$', views.academicduration, name='academicduration'),
        #url(r'^add_contenttype/$', views.add_contenttype, name='add_contenttype'),
        #url(r'^type/$', views.contentstype, name='contentstype'),
        #url(r'^contents/$', views.contents, name='contents'),
        #url(r'^permissions/$', views.permissions, name='permissions'),
        url(r'^contenttype/$', views.contenttype_list, name='contenttype_list'),
        url(r'^contenttype/new$', views.contenttype_create, name='contenttype_new'),
        url(r'^contenttype/edit/(?P<pk>\d+)$', views.contenttype_update, name='contenttype_edit'),
        url(r'^contenttype/delete/(?P<pk>\d+)$',views.contenttype_delete, name='contenttype_delete'),
        )