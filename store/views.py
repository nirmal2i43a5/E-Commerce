from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .codeuse import cookieCart,cartData

# Create your views here.

def store(request):
	
	if request.user.is_authenticated:
		cart_data = cartData(request)
		cartItems = cart_data['cartItems']
		order = cart_data['order']
		items = cart_data['items']
  	
	else:
		#Create empty cart for now for non-logged in user
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)



def cart(request):#we have to handle cart for both login and non login user
	if request.user.is_authenticated:
		cart_data = cartData(request)
		cartItems = cart_data['cartItems']
		order = cart_data['order']
		items = cart_data['items']
  
	else:
		#Create empty cart for now for non-logged in user
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']
  
		

	context = {'items':items,'order':order,'cartItems':cartItems}#this is the order of above created in line 16
	return render(request,'store/cart.html',context)

def checkout(request):
	if request.user.is_authenticated:
		cart_data = cartData(request)
		cartItems = cart_data['cartItems']
		order = cart_data['order']
		items = cart_data['items']
  
	else:
		#Create empty cart for now for non-logged in user
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']

	context = {'items':items,'order':order,'cartItems':cartItems}#this is the order of above created in line 16
	return render(request,'store/checkout.html',context)
	



def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action---------------:', action)
	print('Product-----------------:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':#both for add to cart and cart quantity update
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id
  
  
		#below to confirm total
		if total == order.get_cart_total:
			order.complete = True
		order.save()
  
		if order.shipping == True:
			ShippingAddress.objects.create(
			customer=customer,
			order=order,
			address=data['shipping']['address'],
			city=data['shipping']['city'],
			state=data['shipping']['state'],
			zipcode=data['shipping']['zipcode'],
			)
	else:
		print('User is not logged in')

	return JsonResponse('Payment submitted..', safe=False)