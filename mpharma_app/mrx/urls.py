from django.conf.urls import patterns, url

from mrx import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^portal/$', views.portal, name='portal'),
	url(r'^doctor/$', views.doctor, name='doctor'),
	url(r'^addPhys/$', views.addPhys, name='addPhys'),
	url(r'^addPat/$', views.addPat, name='addPat'),
	url(r'^addPharm/$', views.addPharm, name='addPharm'),
)