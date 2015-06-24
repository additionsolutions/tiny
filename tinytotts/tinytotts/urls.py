from django.conf.urls import patterns, include, url
from django.contrib import admin
from base import views
from django.conf import settings
    
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tinytotts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^addsol/', include(admin.site.urls)),
    url(r'^aboutus/', views.aboutus, name='aboutus'),
    url(r'^excelencia/', views.excelencia, name='excelencia'),
    url(r'^qna/', views.qna, name='qna'),
    url(r'^c/', include('contents.urls')),
    url(r'^t/', include('etests.urls')),
    url(r'^m/', include('messaging.urls')),
    #url(r'^dmin/', include('dmin.urls')),
    url(r'^a/', include('dmin.urls')),
    url(r'^base/', include('base.urls')),
    url(r'^$', include('base.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^accounts/password_change/$','django.contrib.auth.views.password_change',			{'post_change_redirect' : '/accounts/password_change/done/'}, name="password_change"), 
    url(r'^accounts/password_change/done/$', 
        'django.contrib.auth.views.password_change_done'),
)
