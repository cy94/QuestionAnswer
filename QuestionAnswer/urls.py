from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from QuestionAnswer import views

urlpatterns = patterns('',
	# /QuestionAnswer/
	url(r'^$', views.IndexView.as_view(), name='index'),
	# /QuestionAnswer/1
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	# /QuestionAnswer/1/view_answer
	url(r'^(?P<question_id>\d+)/view_answer/$', views.view_answer, name='view_answer'),
	# /QuestionAnswer/new_question
	url(r'^new_question/$', views.new_question, name='new_question'),
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)

urlpatterns += staticfiles_urlpatterns()
