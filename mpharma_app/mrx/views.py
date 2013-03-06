from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import *
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.hashers import *
from twilio.rest import TwilioRestClient

from mrx.models import *

def index(request):
    return render(request, 'mrx/index.jade')

def addRx(request):
	if request.method == "POST":		
		if check_password(request.POST['password'], request.user.password):			
			try:
				pat = Patient.objects.get(patient_phone=request.POST['tel'])
				drug = Drug.objects.get(drug_NDC=request.POST['NDC'])
			except	(KeyError, Patient.DoesNotExist, Drug.DoesNotExist):
					phys = request.user
					rosterList = phys.physician.roster_set.all()
					rx_array = []
					for p in rosterList:
						rx = p.patient.rx_set.all()
						for r in rx:
							rx_array.append(r)
					return render(request, 'mrx/Doctor.jade', {
						'phys': request.user,
						'error_message': "That patient is not in our database",
						'roster':rosterList,
						'rx_array':rx_array,
					})
			else:
				rx = Rx(patient=pat, drug=drug, instructions=request.POST['instructions'])
				rx.save()
				client = TwilioRestClient(account = 'AC2fb492594a820e21c4c95183ce0826c8',token = 'eb7cbcd43dbca3fc054c4c33c0b96407')
				message = client.sms.messages.create(to=pat.patient_phone, from_="+1 339-224-6402",
				                                     body="Hi "+pat.patient_user.first_name+",\n CVS\n701 Portola Dr\n San Francisco, CA 94127\n(415) 504-6043\n has "+ drug.drug_name+" for $97.50.\nCourtesy,\nMPharma")
				return HttpResponseRedirect(reverse('mrx:doctor'))
		else:
			return HttpResponseRedirect(reverse('mrx:doctor'))
	else:
		return HttpResponseRedirect(reverse('mrx:index'))
		
	
def addPharm(request):
	if request.method == "POST":
		user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
		user.save()
		pharm = Pharmacy(
			# physician_firstName = request.POST['first_name'],
			# physician_lastName = request.POST['last_name'],
			# physician_password = request.POST['password'],
			pharmacy_user = user,
			pharmacy_name = request.POST['name'],
			pharmacy_phone = request.POST['tel'],
			pharmacy_country = request.POST['country'],
			pharmacy_province = request.POST['state'],
			pharmacy_city = request.POST['city'],
			pharmacy_street = request.POST['street'],
			pharmacy_street_number = request.POST['streetNo'],
		)
		pharm.save()
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('mrx:pharm'))
	else:
		return HttpResponseRedirect(reverse('mrx:index'))
		
def addPat(request):
	if request.method == "POST":
		user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
		user.last_name = request.POST['last_name']
		user.first_name = request.POST['first_name']
		user.save()
		pat = Patient(
			# physician_firstName = request.POST['first_name'],
			# physician_lastName = request.POST['last_name'],
			# physician_password = request.POST['password'],
			patient_user = user,
			patient_phone = request.POST['tel'],
			patient_country = request.POST['country'],
			patient_province = request.POST['state'],
			patient_city = request.POST['city'],
		)
		pat.save()
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('mrx:pat'))
	else:
		return HttpResponseRedirect(reverse('mrx:index'))
		
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
		return HttpResponseRedirect(reverse('mrx:index'))
		
def doctor(request):
	if hasattr(request.user, 'physician'):
		phys = request.user
		rosterList = phys.physician.roster_set.all()
		rx_array = []
		for p in rosterList:
			rx = p.patient.rx_set.all()
			for r in rx:
				rx_array.append(r)
		return render(request, 'mrx/Doctor.jade', {'phys': phys, 'roster':rosterList, 'rx_array':rx_array})
	else:
		return HttpResponseRedirect(reverse('mrx:index'))
	
def pat(request):
	if hasattr(request.user, 'patient'):
		pat = request.user
		print pat
		return render(request, 'mrx/Pat.jade', {'pat': pat})
	else:
		return HttpResponseRedirect(reverse('mrx:index'))
		
	
def pharm(request):
	if hasattr(request.user, 'pharmacy'):
		pharm = request.user
		print pharm
		return render(request, 'mrx/Pharm.jade', {'pharm': pharm})
	else:
		return HttpResponseRedirect(reverse('mrx:index'))

# Note you haven't done anything with super user... perhaps for demo good idea, but otherwise superuser is just system admin...
def sup(request):
	sup = request.user
	print sup
	return render(request, 'mrx/Pharm.jade', {'sup': sup})
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
				elif hasattr(request.user, 'patient'):
					return HttpResponseRedirect(reverse('mrx:pat'))
				elif hasattr(request.user, 'pharmacy'):
					return HttpResponseRedirect(reverse('mrx:pharm'))
				elif user.is_superuser:
					return HttpResponseRedirect(reverse('mrx:sup'))
				# elif has patient, pharmacy, etc.
			else:
				return HttpResponseRedirect(reverse('mrx:index'))
				# Return a 'disabled account' error message
		else:
			return HttpResponseRedirect(reverse('mrx:index'))
			# Return an 'invalid login' error message.
	else:
		return HttpResponseRedirect(reverse('mrx:index'))
		
def addToRoster(request):
	try:
		pat = Patient.objects.get(patient_phone=request.POST['tel'])
	except	(KeyError, Patient.DoesNotExist):
			#redisplay the poll voting form
			phys = request.user
			rosterList = phys.physician.roster_set.all()
			return render(request, 'mrx/Doctor.jade', {
				'phys': request.user,
				'error_message': "That patient is not in our database",
				'roster':rosterList,
			})
	else:
		roster = Roster(physician=request.user.physician, patient=pat)
		roster.save()
		return HttpResponseRedirect(reverse('mrx:doctor'))
			

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('mrx:index'))