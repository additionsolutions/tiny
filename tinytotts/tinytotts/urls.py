from django.conf.urls import patterns, include, url
from django.contrib import admin
from base import views
    
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tinytotts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^addsol/', include(admin.site.urls)),
    url(r'^aboutus/', views.aboutus, name='aboutus'),
    url(r'^tinytotts/', views.tinytotts, name='tinytotts'),
    url(r'^c/', include('contents.urls')),
    url(r'^base/', include('base.urls')),
    url(r'^$', include('base.urls')),
)
