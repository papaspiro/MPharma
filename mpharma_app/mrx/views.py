from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from mrx.models import *

def index(request):
    return render(request, 'mrx/index.jade')

def addPhys(request):
	if request.method == "POST":
		phys = Physician(
			physician_firstName = request.POST['first_name'],
			physician_lastName = request.POST['last_name'],
			physician_password = request.POST['password'],
			physician_phone = request.POST['tel'],
			physician_hospital = request.POST['hosp_name'],
			physician_country = request.POST['country'],
			physician_province = request.POST['state'],
			physician_city = request.POST['city'],
		)
		phys.save()
		return HttpResponseRedirect(reverse('mrx:doctor', args=(phys.pk,)))
	else:
		render(request, 'mrx/index.jade')
		
def doctor(request, phys_id):
	phys = get_object_or_404(Physician, pk=phys_id)
	return render(request, 'mrx/Doctor.jade', {'phys': phys})
	

	
