
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.template.loader import render_to_string
from store.models import Product

def search_store(request):	
	data = dict()
	field_value = request.GET.get('query')
	print(field_value)
	
	if field_value:
		products = Product.objects.filter(name__icontains = field_value)
		data['html_list'] = render_to_string('store/get_search_products.html',{'products':products},request = request)
		
		return JsonResponse(data=data,safe=False)
	else:
		products = Product.objects.all()
	   
		context = {'products': products}
		data['html_list'] = render_to_string('store/get_search_products.html',context,request=request)

		return JsonResponse(data=data,safe=False)

def search(request,template_name,category):
	
	data = dict()
	field_value = request.GET.get('query')
 
	
	if field_value:
		# products = Product.objects.filter(category='Camera').filter(name__icontains = field_value)
		products = Product.objects.filter(category=category).filter(name__icontains = field_value)
		data['html_list'] = render_to_string(template_name,{'products':products},request = request)
		
		return JsonResponse(data)

	else:
		products = Product.objects.filter(category=category)
	   
		context = {'products': products}
		data['html_list'] = render_to_string(template_name,context,request=request)

		return JsonResponse(data)



def search_cameras(request):
	return search(request,'category/electronics_devices/cameras/get_search_cameras.html','Camera')

def search_laptops(request):
    	return search(request,'category/electronics_devices/laptops/get_search_laptops.html','Laptop')
 
def search_mobiles(request):
    	return search(request,'category/electronics_devices/mobiles/get_search_mobiles.html','Mobile')
 
 
def search_womens(request):
    	return search(request,'category/sports_outdoors/ladies/get_search_ladies.html','Womens shoes and clothing')
 
def search_mens(request):
    	return search(request,'category/sports_outdoors/mens/get_search_mens.html','Mens shoes and clothing')

	
