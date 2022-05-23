from django import forms
from .models import *

class MedicineForm(forms.ModelForm):
	
	class Meta:
		model = Medicine
		fields = ('dateRegistered','category', 'genericName', 'commonBrand','manufacturedDate','expiryDate',
				  'size','price','number','use','effects',)

		#fields = '__all__'


class CustomerForm(forms.ModelForm):
	
	class Meta:
		model = Customer
		fields = ('firstName','middleName','lastName','birthdate')


class CartForm(forms.ModelForm):
	
	class Meta:
		model = Cart
		fields = ('cust','meds','name','unit_price','quantity',)