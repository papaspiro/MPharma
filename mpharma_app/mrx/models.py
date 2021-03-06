from django.db import models

from django.contrib.auth.models import User, Group, Permission

# Create your models here.
class Pharmacy(models.Model):
	pharmacy_user = models.OneToOneField(User, related_name='pharmacy', primary_key=True)
	pharmacy_phone = models.CharField(max_length=15)
	pharmacy_name = models.CharField(max_length=100)
	pharmacy_country = models.CharField(max_length=100)
	pharmacy_province = models.CharField(max_length=100)
	pharmacy_city = models.CharField(max_length=100)
	pharmacy_street = models.CharField(max_length=100)
	# pharmacy_email = models.CharField(max_length=100)
	# pharmacy_username = models.CharField(max_length=100)
	pharmacy_street_number = models.IntegerField(max_length=10, null=True)
	# pharmacy_lat = models.DecimalField(max_digits=10, decimal_places=7, null=True)
	# pharmacy_long = models.DecimalField(max_digits=10, decimal_places=7, null=True)
	
	def __unicode__(self):
		return self.pharmacy_name
		
class Drug(models.Model):
	# drug_id = models.PositiveIntegerField(primary_key=True, max_length=10) have to add drug id at somepoint...
	drug_NDC = models.CharField(max_length=100, primary_key=True)
	drug_name = models.CharField(max_length=100)
	drug_dosage = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.drug_name
		
class Inventory(models.Model):
	pharmacy = models.ForeignKey(Pharmacy)
	drug = models.ForeignKey(Drug)
	quantity = models.PositiveIntegerField(max_length=15, default=0)
	
	def __unicode__(self):
		return (self.pharmacy_id, self.drug_id, self.quantity)
		
class Patient(models.Model):
	# patient_firstName = models.CharField(max_length=100)
	# patient_lastName = models.CharField(max_length=100)
	# patient_username = models.CharField(max_length=100)
	# patient_password = models.CharField(max_length=100)
	patient_user = models.OneToOneField(User, related_name='patient', primary_key=True)
	patient_phone = models.CharField(max_length=15, null=True)
	patient_country = models.CharField(max_length=100)
	patient_province = models.CharField(max_length=100)
	patient_city = models.CharField(max_length=100)
	# patient_email = models.CharField(max_length=100)
	# patient_street = models.CharField(max_length=100)
	# pharmacy_street_number = models.IntegerField(max_length=10, null=True)
	def __unicode__(self):
		return (self.patient_user)
	
class Physician(models.Model):
	# physician_id = models.PositiveIntegerField(primary_key=True, max_length=10)
	# physician_firstName = models.CharField(max_length=100)
	# physician_lastName = models.CharField(max_length=100)
	# physician_password = models.CharField(max_length=100)
	# physician_phone = models.CharField(max_length=15, null=True)
	physician_user = models.OneToOneField(User, related_name='physician', primary_key=True)
	physician_hospital = models.CharField(max_length=100)
	physician_country = models.CharField(max_length=100)
	physician_province = models.CharField(max_length=100)
	physician_city = models.CharField(max_length=100)
	# physician_email = models.CharField(max_length=100)
	# physician_username = models.CharField(max_length=100)
	# physician_street = models.CharField(max_length=100)
	# pharmacy_street_number = models.IntegerField(max_length=10, null=True)
	def __unicode__(self):
		return (self.physician_user)
	
class Rx(models.Model):
	patient = models.ForeignKey(Patient)
	drug = models.ForeignKey(Drug)
	remaining = models.PositiveIntegerField(max_length=10, default=0)
	daily = models.BooleanField(default=False)
	instructions = models.CharField(max_length=300)
	def __unicode__(self):
		return (self.patient, self.drug)
	
class Roster(models.Model):
	physician = models.ForeignKey(Physician)
	patient = models.ForeignKey(Patient)
	# isActive = models.BooleanField(default=True)
	def __unicode__(self):
		return (self.physician.physician_hospital, self.patient.patient_country)
	