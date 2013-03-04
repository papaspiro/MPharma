from django.conf.urls import patterns, url

from mrx import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^physician/$', views.physician, name='physician')
)