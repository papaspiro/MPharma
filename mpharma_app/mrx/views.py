from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import *
from django.contrib.auth.models import User, Group, Permission

from mrx.models import *

def index(request):
    return render(request, 'mrx/index.jade')

# NEED addPharm and addPat they are basically the same as addphys... then you need to add patient and pharmacy landing pages and direct
#users to those pages through the portal... 

def addPhys(request):
	if request.method == "POST":
		user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
		user.last_name = request.POST['last_name']
		user.first_name = request.POST['first_name']
		user.save()
		phys = Physician(
			# physician_firstName = request.POST['first_name'],
			# physician_lastName = request.POST['last_name'],
			# physician_password = request.POST['password'],
			physician_user = user,
			physician_hospital = request.POST['hosp_name'],
			physician_country = request.POST['country'],
			physician_province = request.POST['state'],
			physician_city = request.POST['city'],
		)
		phys.save()
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('mrx:doctor'))
	else:
		render(request, 'mrx/index.jade')
		
def doctor(request):
	phys = request.user
	print phys
	return render(request, 'mrx/Doctor.jade', {'phys': phys})

	# Idea here is to ffigure out what type of user user is by hasattr or whatever user if has attr...
	# add conditionals then shoot out to different landing pages
	# so... must add drop down with username password form in index that has action "portal" in index.jade
	
def portal(request):
	if request.method == "POST":
		username = request.POST['log_username']
		password = request.POST['log_password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				if hasattr(request.user, 'physician'):
					return HttpResponseRedirect(reverse('mrx:doctor'))
					# Redirect to a success page.
				# elif has patient, pharmacy, etc.
			else:
				return HttpResponseRedirect(reverse('mrx:index'))
				# Return a 'disabled account' error message
		else:
			return HttpResponseRedirect(reverse('mrx:index'))
			# Return an 'invalid login' error message.
	else:
		return HttpResponseRedirect(reverse('mrx:index'))
