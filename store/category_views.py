
from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .codeuse import cookieCart,cartData,guestOrder
from django.db.models import Q
from django.template.loader import render_to_string

def mens_items(request):
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

	

	products = Product.objects.filter(category='Mens shoes and clothing')#render only electric item products
	products_count = products.count()

	context = {'products':products, 'cartItems':cartItems,'items':items,'products_count':products_count}
	return render(request, 'category/sports_outdoors/mens.html', context)


def womens_items(request):
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

	

	products = Product.objects.filter(category='Womens shoes and clothing')#render only electric item products
	products_count = products.count()

	context = {'products':products, 'cartItems':cartItems,'items':items,'products_count':products_count}
	return render(request, 'category/sports_outdoors/ladies.html', context)



def laptops(request):
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

	

	products = Product.objects.filter(category='Laptop')#render only electric item products
	products_count = products.count()

	context = {'products':products, 'cartItems':cartItems,'items':items,'products_count':products_count}
	return render(request, 'category/electronics_devices/laptop.html', context)


def cameras(request):
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

	

	products = Product.objects.filter(category='Camera')#render only electric item products
	products_count = products.count()

	context = {'products':products, 'cartItems':cartItems,'items':items,'products_count':products_count}
	return render(request, 'category/electronics_devices/cameras/camera.html', context)

def search_cameras(request):
	
	data = dict()
	field_value = request.GET.get('query')
	
	if field_value:
		
  
		products = Product.objects.filter(category='Camera').filter(name__icontains = field_value)
		data['html_list'] = render_to_string('category/electronics_devices/cameras/get_search_cameras.html',{'products':products},request = request)
		
		return JsonResponse(data)

	else:
		products = Product.objects.filter(category="Camera")
	   
		context = {'products': products}
		data['html_list'] = render_to_string('category/electronics_devices/cameras/get_search_cameras.html',context,request=request)

		return JsonResponse(data)


def mobiles(request):
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

	

	products = Product.objects.filter(category='Mobile')#render only electric item products
	products_count = products.count()

	context = {'products':products, 'cartItems':cartItems,'items':items,'products_count':products_count}
	return render(request, 'category/electronics_devices/mobile.html', context)


