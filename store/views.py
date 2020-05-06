from django.shortcuts import render

from .models import Product,Order

# Create your views here.

def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request,'store/store.html',context)

def cart(request):#we have to handle cart for both login and non login user
	
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()#particular order id items=>order is created with its id one customer many order
  
	else:
		#Create empty cart for now for non-logged in user
		items = []
		#to create an object for Non logged in users. 
		order = {'get_cart_total':0,'get_cart_items':0}
	 

	context = {'items':items,'order':order}#this is the order of above created in line 16
 
	return render(request,'store/cart.html',context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
  
	else:
		#Create empty cart for now for non-logged in user
		items = []
		#to create an object for Non logged in users. 
		order = {'get_cart_total':0,'get_cart_items':0}
	 

	context = {'items':items,'order':order}#this is the order of above created in line 16
 


	return render(request,'store/checkout.html',context)
	


