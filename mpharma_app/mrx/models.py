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
	pharmacy_id = models.ForeignKey(Pharmacy)
	drug_id = models.ForeignKey(Drug)
	quantity = models.PositiveIntegerField(max_length=15, default=0)
	
	def __unicode__(self):
		return (self.pharmacy_id, self.drug_id, self.quantity)
		
class Patient(models.Model):
	patient_name = models.CharField(max_length=100)
	patient_phone = models.PositiveIntegerField(max_length=15, null=True)
	