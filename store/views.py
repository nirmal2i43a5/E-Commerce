from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
import json
import datetime
from .models import *
from .codeuse import cookieCart,cartData,guestOrder
from django.db.models import Q
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

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
	products_count = products.count()

	# products = Product.objects.filter(category='Electric items')#render only electric item products
	
	context = {'products':products, 'cartItems':cartItems,'items':items,'products_count':products_count}
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


@login_required(login_url='/login')#required for non login user
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
	print(transaction_id)
	data = json.loads(request.body)
	

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])#it the total price after checkout

	order.transaction_id = transaction_id

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

	return JsonResponse('Payment submitted.(response from processOrder views)', safe=False)





def product_view(request, pk):
	#below is to show particular product details
	product = Product.objects.get(id=pk)
	if request.method == 'POST':
		return redirect('store_app:view',pk=pk)

	#below code id just to show quantity in the cart for both login and nonlogin user
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

	context = {'product':product,
            'cartItems':cartItems,
            'items':items#this is for plus and minus sign to work in desc page
            }
 
	return render(request, 'store/product_desc.html', context)

#i also want to show cart total num in view page


# def delete(request,pk):
#     product = get_object_or_404(Product,pk = pk)
#     product.delete()
#     return redirect('/store')

    
    


	





	
	