
from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .codeuse import cookieCart,cartData,guestOrder
from django.db.models import Q
from django.template.loader import render_to_string

def particular_items(request,template_name,particular_category):
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

	

	products = Product.objects.filter(category=particular_category)#render only electric item products
	products_count = products.count()

	context = {'products':products, 'cartItems':cartItems,'items':items,'products_count':products_count}
 
	return render(request, template_name, context)

def mens_items(request):
	
	return particular_items(request, 'category/sports_outdoors/mens/mens.html','Mens shoes and clothing' )


def womens_items(request):
	return particular_items(request, 'category/sports_outdoors/ladies/ladies.html', 'Womens shoes and clothing')


def laptops(request):
	return particular_items(request, 'category/electronics_devices/laptops/laptop.html', 'Laptop')


def cameras(request):
	return particular_items(request, 'category/electronics_devices/cameras/camera.html','Camera')


def mobiles(request):
	
	return particular_items(request, 'category/electronics_devices/mobiles/mobile.html', 'Mobile')


