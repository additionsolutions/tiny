from django.conf.urls import patterns, url
from dmin import views

urlpatterns = patterns('',
	url(r'^$', views.user_login, name='basic'),
        #url(r'^dmin/$', views.basic, name='basic'),
        #url(r'^dmin/user$', views.UserListView.as_view(), name='userlist'),
	url(r'^dmin/user$', views.user_list, name='userlist'),
	url(r'^dmin/login/$', views.user_login, name='login'),
	url(r'^dmin/logout/$', views.user_logout, name='logout'),
	url(r'^dmin/profile/$', views.profile, name='admin_profile'),
	url(r'^dmin/user/edit/(?P<pk>\d+)$', views.user_update, name='user_edit'),
        url(r'^dmin/user/delete/(?P<pk>\d+)$', views.user_delete, name='user_delete'),
	url(r'^dmin/register/$', views.register, name='dmin_register'),
	url(r'^dmin/groups/$', views.group_list, name='group_list'),
	url(r'^dmin/groups/new$', views.group_create, name='group_new'),
	url(r'^dmin/groups/edit/(?P<pk>\d+)$', views.group_update, name='groups_edit'),
	url(r'^dmin/groups/delete/(?P<pk>\d+)$', views.group_delete, name='groups_delete'),
	url(r'^dmin/contenttype/$', views.contenttype_list, name='contenttype_list'),
	url(r'^dmin/contenttype/new$', views.contenttype_create, name='conttype_new'),
	url(r'^dmin/contenttype/edit/(?P<pk>\d+)$', views.contenttype_update, name='conttype_edit'),
        url(r'^dmin/contenttype/delete/(?P<pk>\d+)$',views.contenttype_delete, name='conttype_delete'),
	url(r'^dmin/content/$', views.content_list, name='cont_list'),
	url(r'^dmin/content/new$', views.content_create, name='cont_new'),
        url(r'^dmin/content/edit/(?P<pk>\d+)$', views.content_update, name='cont_edit'),
        url(r'^dmin/content/delete/(?P<pk>\d+)$',views.content_delete, name='cont_delete'),
	url(r'^dmin/testset/$', views.testset, name='testset'),
	url(r'^dmin/testset/new$', views.testset_create, name='testset_new'),
	url(r'^dmin/testset/edit/(?P<pk>\d+)$', views.testset_update, name='testset_edit'),
        url(r'^dmin/testset/delete/(?P<pk>\d+)$', views.testset_delete, name='testset_delete'),
	url(r'^dmin/testsetline/$', views.testq, name='testq'),
	url(r'^dmin/testsetline/new$', views.testsetline_create, name='testsetline_new'),
	url(r'^dmin/markreport/$', views.report_marks, name='markrpt'),
	url(r'^dmin/userreport/$', views.report_userwisemarks, name='userrpt'),
	url(r'^dmin/scorecard/(\d{1,2})/(\d{1,2})$',views.get_scorecard, name='get_scorecard'),
	url(r'^dmin/testsetline_testset/$',views.gettestsetlinefromtestset, name='gettestsetlinefromtestset'),
	url(r'^dmin/testsetlinedisplay/(\d{1,2})/$',views.get_testsetline, name='get_testsetline'),
	url(r'^dmin/testsetline/edit/(?P<pk>\d+)$', views.testsetline_update, name='testsetline_edit'),
 url(r'^dmin/testsetline/delete/(?P<pk>\d+)$', views.testsetline_delete, name='testsetline_delete'),
	url(r'^dmin/content_contenttype/$', views.getcontentfromcontettype, name='getcontentfromcontettype'),
	url(r'^dmin/contentdisplay/(\d{1,2})/$',views.get_content, name='get_content'),
	url(r'^dmin/category/$', views.category_list, name='category_list'),
	url(r'^dmin/category/new$', views.category_create, name='category_new'),
	url(r'^dmin/category/edit/(?P<pk>\d+)$', views.category_update, name='category_edit'),
	url(r'^dmin/question/$', views.question_list, name='question_list'),
	url(r'^dmin/question/new$', views.question_create, name='question_new'),
	url(r'^dmin/question/edit/(?P<pk>\d+)$', views.question_update, name='question_edit'),
	url(r'^dmin/option/$', views.option_list, name='option_list'),
	url(r'^dmin/optiondisplay/(\d{1,2})/$',views.get_option, name='get_option'),
	url(r'^dmin/option/new$', views.option_create, name='option_new'),
	url(r'^dmin/option/edit/(?P<pk>\d+)$', views.option_update, name='option_edit'),
        url(r'^dmin/option/delete/(?P<pk>\d+)$', views.option_delete, name='option_delete'),
	url(r'^dmin/radiotest/$', views.radio_test, name='radio_test'),
	url(r'^dmin/summaryreport/$', views.userwise_summaryreport, name='userwise_summaryreport'),
	url(r'^dmin/summary/(\d{1,2})$',views.get_summaryreport, name='get_summaryreport'),
    url(r'^dmin/testsetuser_flag/$', views.testsetuser_flag, name='user_flag'),
        )
