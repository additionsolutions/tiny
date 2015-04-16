from django.conf.urls import patterns, url
from etests import views

urlpatterns = patterns('',
        url(r'^etest/$', views.etest, name='etest'),
        url(r'^etest/(\d{1,2})/$', views.etest, name='etest'),
        url(r'^etest/testlist$', views.testlist, name='testlist'),
        url(r'^etest/sr/(\d{1,2})/$', views.etestsr, name='etestsr'),
        url(r'^etest/ans/(\d{1,2})/$', views.etestans, name='etestans'),
        )