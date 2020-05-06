 
from django.urls import path

from . import views

app_name = 'store_app'

urlpatterns = [
	#Leave as empty string for base url
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

]