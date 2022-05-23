from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from .models import *
import speech_recognition as sr 
# import pyttsx3  
import os

# Create your views here.


#Garcia, LT code part
class DashboardView(View):
	def get(self, request):
		medicines = Medicine.objects.all()
		customers = Customer.objects.all()
		cart = Cart.objects.all()
		context = {
			'medicines' : medicines,
			'customers' : customers,
			'cart' : cart,
		}
		return render(request,'dashboard.html', context)

	def post(self, request):
		if request.method == 'POST':
			if 'updateBtn' in request.POST:
				#form = MedicineForm(request.POST,request.FILES)
				mid = request.POST.get("medicine-id")
				date_register = request.POST.get("medicine-dateRegistered")
				category = request.POST.get("medicine-category")
				sku = request.POST.get("medicine-sku")
				generic = request.POST.get("medicine-genericName")
				brand = request.POST.get("medicine-commonBrand")
				man_date = request.POST.get("medicine-manufacturedDate")
				ex_date = request.POST.get("medicine-expiryDate")
				size = request.POST.get("medicine-size")
				price = request.POST.get("medicine-price")
				items = request.POST.get("medicine-number")
				use  = request.POST.get("medicine-use")
				effects = request.POST.get("medicine-effects")
				image1 = request.FILES.get('medicine-image1', None)
				image2 = request.FILES.get('medicine-image2', None)
				image3 = request.FILES.get('medicine-image3', None)

				if image1 is not None:
					form = Medicine.objects.get(id = mid)
					form.image1 = image1
					form.save()

				if image2 is not None:
					form = Medicine.objects.get(id = mid)
					form.image2 = image2
					form.save()

				if image3 is not None:
					form = Medicine.objects.get(id = mid)
					form.image3 = image3
					form.save()

				Medicine.objects.filter(id = mid).update(dateRegistered=date_register, category = category, sku_value = sku, genericName = generic, commonBrand =brand,
				 			 manufacturedDate = man_date, expiryDate = ex_date, size = size, price = price, number = items,
				 			  use = use, effects = effects)

				messages.info(request, 'INFO UPDATE SUCCESSFUL')
				return redirect ("pharmacy:dashboard_view")
			
			elif 'deleteBtn' in request.POST:
				mid = request.POST.get("med-id")
				cart = Cart.objects.all()
				customer = Customer.objects.all()
				medicines = Medicine.objects.get(id=mid)

				for c in cart:
					for ct in customer:
						if c.cust == ct.id: 
							if c.meds == medicines.id:
								cartid = c.id
								Cart.objects.filter(id = cartid).delete()

				Medicine.objects.filter(id = mid).delete()

				messages.info(request, 'INFO DELETE SUCCESSFUL')
				return redirect ("pharmacy:dashboard_view")

			#CART FUNCTIONALITIES
			elif 'buyBtn' in request.POST: #THIS IS THE ADD TO CART
				form = CartForm(request.POST,request.FILES)

				#MANUALLY ADD CUSTOMER ID JUST FOR THE PURPOSE OF AN EXAMPLE
				cid = 1

				mid = request.POST.get("medicine-id")
				medicines = Medicine.objects.get(id=mid)
				name = medicines.genericName
				image = medicines.image3
				unit_price = medicines.price
				quantity = 0
				if Cart.objects.filter(name = name).exists():
					quantity = medicines.number
					quantity += 1
					medicines.number = quantity
					messages.warning(request, 'MEDICINE ALREADY EXIST IN THE CART')
				else:
					quantity += 1

					num = medicines.number 

					num -= 1
					Medicine.objects.filter(id = mid).update(number = num)

					form = Cart(cust=cid, meds=mid, name=name,image=image, unit_price = unit_price, quantity=quantity)
					
					form.save()

					messages.info(request, 'Medicine Added to Cart')
				return redirect ("pharmacy:dashboard_view")

			elif 'cartDelete' in request.POST:
				cartid = request.POST.get("cart-id")
				cart = Cart.objects.get(id=cartid)
				med = Medicine.objects.all()
				
				for m in med:
					if cart.meds == m.id:
						quantity = m.number
						quantity += 1
						m.number =  quantity
						m.save()

						Cart.objects.filter(id = cartid).delete()


						messages.info(request, 'ITEM DELETED SUCCESSFULLY')
				return redirect ("pharmacy:dashboard_view")

			# AFTER THE CUSTOMER PAYS THE MEDICINE THEY ADDED TO CART
			# THEN THE ITEMS IN THE CART DB WILL BE DELETED AND THE MEDICINE
			# ID WILL BE STORED TO THE MANYTOMANY FIELD IN THE CUSTOMER DB
			
			elif 'payBtn' in request.POST:
				cid = request.POST.get("ct-id")
				medicines = Medicine.objects.all()
				customer = Customer.objects.all()
				cart = Cart.objects.all()

				quan = request.POST.get("quantity")
				
				for c in cart:
					for ct in customer:
						if c.cust == ct.id: 
							for m in medicines:
								if c.name == m.genericName:
									qt = m.number + 1
									qt -= int(quan)
									m.number = qt
									m.save()
									ct.medicine.add(m.id)

				Cart.objects.filter(cust = cid).delete()

				messages.info(request, 'PAID')
				return redirect ("pharmacy:dashboard_view")

			#CUSTOMER UPDATE DELETE
			elif 'btnUpdate' in request.POST:
				print('update profile button clicked')
				cid = request.POST.get("customerId")
				fname = request.POST.get("firstName")
				mname = request.POST.get("middleName")
				lname = request.POST.get("lastName")
				st = request.POST.get("street")
				brgy = request.POST.get("barangay")
				cty = request.POST.get("city")
				zcode = request.POST.get("zipcode")
				prov = request.POST.get("province")
				cntry = request.POST.get("country")
				bday = request.POST.get("birthdate")
				hght = request.POST.get("height")
				wght = request.POST.get("weight")
				rlgn = request.POST.get("religion")
				gndr = request.POST.get("gender")
				sttus = request.POST.get("status")
				spName = request.POST.get("spouseName")
				spOcc = request.POST.get("spouseOcc")	
				momName = request.POST.get("mother")
				momOcc = request.POST.get("motherOcc")
				dadName = request.POST.get("father")
				dadOcc = request.POST.get("fatherOcc")
				update_customer = Customer.objects.filter(person_ptr_id = cid).update(firstName=fname, middleName=mname, lastName=lname, 
					street=st, barangay=brgy, city=cty, zipcode=zcode,  province=prov, country=cntry, birthdate=bday, height=hght,
					weight=wght, religion=rlgn, gender=gndr, status=sttus, spouseName=spName, spouseOccupation=spOcc, motherName=momName,
					motherOccupation=momOcc, fatherName=dadName, fatherOccupation=dadOcc)
				print(update_customer)
				print('profile updated')

				messages.info(request, 'INFO UPDATE SUCCESSFUL')
				return redirect ("pharmacy:dashboard_view")

			elif 'btnDelete' in request.POST:	
				print('delete button clicked')
				cid = request.POST.get("ccustomerId")
				cust = Customer.objects.filter(person_ptr_id=cid).delete()
				pers = Person.objects.filter(id = cid).delete()
				print('recorded deleted')

				messages.info(request, 'INFO DELETE SUCCESSFUL')
				return redirect ("pharmacy:dashboard_view")

			else:
				messages.error(request, 'SORRY. ACTION FAILED')
				return render(request,'dashboard.html')
		else:
			messages.error(request, 'POST INVALID')
			return render(request,'dashboard.html')


class MedicineRegistration(View):
	def get(self, request):
		return render(request,'medicine_registration.html')

	def post(self, request):
		form = MedicineForm(request.POST,request.FILES)

		if form.is_valid():
			date_register = request.POST.get("dateRegistered")
			category = request.POST.get("category")
			sku = request.POST.get("sku")
			generic = request.POST.get("genericName")
			brand = request.POST.get("commonBrand")
			man_date = request.POST.get("manufacturedDate")
			ex_date = request.POST.get("expiryDate")
			size = request.POST.get("size")
			price = request.POST.get("price")
			items = request.POST.get("number")
			use  = request.POST.get("use")
			effects = request.POST.get("effects")
			#image1 = request.FILES['image1']
			image1 = request.FILES.get('image1', None)
			image2 = request.FILES.get('image2', None)
			image3 = request.FILES.get('image3', None)
			#fs = FileSystemStorage()
			#fs.save(image1.name, image1)
			form = Medicine(dateRegistered=date_register, category = category, sku_value = sku, genericName = generic, commonBrand =brand,
							 manufacturedDate = man_date, expiryDate = ex_date, size = size, price = price, number = items,
							  use = use, effects = effects, image1 = image1, image2 = image2, image3 = image3)
			
			form.save()
			messages.success(request, 'FORM SUBMISSION SUCCESSFUL')

			return redirect ("pharmacy:dashboard_view")
			# return render(request,'medicine_registration.html',{'form':form})
		else:
			messages.error(request, 'SORRY. FORM SUBMISSION FAILED. PLEASE TRY AGAIN.')
			return render(request,'medicine_registration.html',{'form':form})

	
#Capangpangan, TML code part
class LandingIndexView(View):
	def get(self, request):
		# customers = Customer.objects.all()
		# print(customers)
		# for customer in customers:
		# 	print(customer)
		# 	print(customer.id)
		# 	print(customer.firstName)
		# 	print(customer.lastName)
		# 	print(customer.profileImage)
		# context = {
		# 	'customers' : customers
		# }

		# return render(request,'ABC.html', context)
		return render(request,'ABC.html')


class CustomerRegistrationView(View):
	def get(self, request):
		return render(request, 'CustReg.html')

	def post(self, request):
		form = CustomerForm(request.POST)
		if form.is_valid():
			#try:
			#dReg = request.POST.get("dateRegistered")
			fname = request.POST.get("firstName")
			mname = request.POST.get("middleName")
			lname = request.POST.get("lastName")
			st = request.POST.get("street")
			brgy = request.POST.get("barangay")
			cty = request.POST.get("city")
			zcode = request.POST.get("zipcode")
			prov = request.POST.get("province")
			cntry = request.POST.get("country")
			bdate = request.POST.get("birthdate")
			hght = request.POST.get("height")
			wght = request.POST.get("weight")
			rlgn = request.POST.get("religion")
			gndr = request.POST.get("gender")
			sttus = request.POST.get("status")
			spName = request.POST.get("spouseName")
			spouseOcc = request.POST.get("spouseOccupation")
			numChil = request.POST.get("noChildren")
			momName = request.POST.get("motherName")
			momOcc = request.POST.get("motherOccupation")
			dadName = request.POST.get("fatherName")
			dadOcc = request.POST.get("fatherOccupation")
			profileImage = request.FILES.get("profileImage")

			form = Customer(firstName = fname, middleName = mname, lastName = lname, street = st,
							barangay = brgy, city = cty, zipcode = zcode, province = prov, country = cntry, birthdate = bdate,
							height = hght, weight = wght, religion = rlgn, gender = gndr, status = sttus, spouseName = spName,
							spouseOccupation = spouseOcc, noChildren = numChil, motherName = momName, motherOccupation = momOcc,
							fatherName = dadName, fatherOccupation = dadOcc, profileImage = profileImage)
			form.save()
			messages.success(request, 'FORM SUBMISSION SUCCESSFUL')
			
			return redirect ("pharmacy:dashboard_view")

		else: 
			print(form.errors)
			return HttpResponse('not valid')
