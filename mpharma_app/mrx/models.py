from django.db import models

# Create your models here.
class Pharmacy(models.Model):
	pharmacy_id = models.PositiveIntegerField(primary_key=True, max_length=10)
	pharmacy_name = models.CharField(max_length=100)
	pharmacy_country = models.CharField(max_length=100)
	pharmacy_province = models.CharField(max_length=100)
	pharmacy_city = models.CharField(max_length=100)
	pharmacy_street = models.CharField(max_length=100)
	pharmacy_street_number = models.IntegerField(max_length=10, null=True)
	pharmacy_lat = models.DecimalField(max_digits=10, decimal_places=7, null=True)
	pharmacy_long = models.DecimalField(max_digits=10, decimal_places=7, null=True)
	
	def __unicode__(self):
		return self.pharmacy_name
		
class Drug(models.Model):
	drug_id = models.PositiveIntegerField(primary_key=True, max_length=10)
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
	patient_firstName = models.CharField(max_length=100)
	patient_lastName = models.CharField(max_length=100)
	patient_password = models.CharField(max_length=100)
	patient_phone = models.PositiveIntegerField(max_length=15, null=True)
	
class Physician(models.Model):
	physician_id = models.PositiveIntegerField(primary_key=True, max_length=10)
	physician_firstName = models.CharField(max_length=100)
	physician_lastName = models.CharField(max_length=100)
	physician_phone = models.PositiveIntegerField(max_length=15, null=True)
	
class Rx(models.Model):
	patient = models.ForeignKey(Patient)
	drug = models.ForeignKey(Drug)
	remaining = models.PositiveIntegerField(max_length=10)
	daily = models.BooleanField(default=False)
	
class Roster(models.Model):
	physician = models.ForeignKey(Physician)
	patient = models.ForeignKey(Patient)
	isActive = models.BooleanField(default=True)
	
	