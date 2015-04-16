from django.conf.urls import patterns, url
from etests import views

urlpatterns = patterns('',
        url(r'^etest/$', views.etest, name='etest'),
        url(r'^etest/sr/(\d{1,2})/$', views.etestsr, name='etestsr'),
        )