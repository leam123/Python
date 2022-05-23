from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
	firstName = models.CharField(max_length = 100)
	middleName = models.CharField(max_length = 100)
	lastName = models.CharField(max_length = 100)
	street = models.CharField(max_length = 100)
	barangay = models.CharField(max_length = 100)
	city = models.CharField(max_length = 100)
	zipcode = models.IntegerField()
	province = models.CharField(max_length = 100)
	country = models.CharField(max_length = 100)
	birthdate = models.DateField()
	height = models.FloatField()
	weight = models.FloatField()
	religion = models.CharField(max_length = 100)
	gender = models.CharField(max_length = 100)
	status = models.CharField(max_length = 100)
	spouseName = models.CharField(max_length = 100)
	spouseOccupation = models.CharField(max_length = 100)
	noChildren = models.IntegerField()
	motherName = models.CharField(max_length = 100)
	motherOccupation = models.CharField(max_length = 100)
	fatherName = models.CharField(max_length = 100)
	fatherOccupation = models.CharField(max_length = 100)
	profileImage = models.ImageField(upload_to='images/', null=True, blank=True)

	class Meta:
		db_table = "Person"


class Medicine(models.Model):

	dateRegistered = models.DateField()
	category = models.CharField(max_length = 50)
	sku_value = models.CharField(max_length = 50)
	genericName = models.CharField(max_length = 20)
	commonBrand = models.CharField(max_length = 20)
	manufacturedDate = models.DateField()
	expiryDate = models.DateField()
	size = models.IntegerField()
	price = models.FloatField() 
	number = models.IntegerField()
	use = models.TextField()
	effects = models.TextField()
	image1 = models.ImageField(upload_to='images/', null=True, blank=True)
	image2 = models.ImageField(upload_to='images/', null=True, blank=True)
	image3 = models.ImageField(upload_to='images/', null=True, blank=True)


	class Meta:
		db_table = "Medicine"

class Customer(Person):
	dateRegistered = models.DateField(default = datetime.now)
	medicine = models.ManyToManyField(Medicine)	#option 200000000000000

	class Meta:		
		db_table = "Customer"



#TEMPORARY TABLE FOR THE MEDICINES THAT THE CUSTOMER ADDED TO CART
class Cart(models.Model):
	cust = models.IntegerField()
	meds = models.IntegerField()
	name =  models.CharField(max_length = 50)
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	unit_price = models.FloatField() 
	quantity = models.IntegerField()

	class Meta:
		db_table = "Cart"