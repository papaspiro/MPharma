from django.conf.urls import patterns, url

from mrx import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	# url(r'^physician/$', views.physician, name='physician'),
	url(r'^(?P<phys_id>\d+)/doctor/$', views.doctor, name='doctor'),
	url(r'^addPhys/$', views.addPhys, name='addPhys'),
)