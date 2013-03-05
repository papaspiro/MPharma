from django.conf.urls import patterns, url

from mrx import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^portal/$', views.portal, name='portal'),
	url(r'^doctor/$', views.doctor, name='doctor'),
	url(r'^sup/$', views.sup, name='sup'),
	url(r'^pat/$', views.pat, name='pat'),
	url(r'^doctor/addToRoster/$', views.addToRoster, name='addToRoster'),
	url(r'^doctor/addRx/$', views.addRx, name='addRx'),
	url(r'^.*/logout/$', views.logout_view, name='logout_view'),
	url(r'^pharm/$', views.pharm, name='pharm'),
	url(r'^addPhys/$', views.addPhys, name='addPhys'),
	url(r'^addPat/$', views.addPat, name='addPat'),
	url(r'^addPharm/$', views.addPharm, name='addPharm'),
)