from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .codeuse import cookieCart,cartData,guestOrder

def Mens_shoes_and_clothing(request):
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

	context = {'products':products, 'cartItems':cartItems,'items':items}
	return render(request, 'category/mens.html', context)

