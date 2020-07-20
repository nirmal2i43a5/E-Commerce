 
from django.urls import path

from . import views,category_views,category_search
from django.views.generic import TemplateView


app_name = 'store_app'

urlpatterns = [
	#Leave as empty string for base url
	path('store/', views.store, name="store"),

	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	 path('update_item/',views.updateItem,name="update_item"),
	#  path('update_view_item/',views.product_view,name="update_item"),
  	#  path('search_update_item/',views.searchUpdateItem,name="search_update_item"),
	path('process_order/',views.processOrder,name = "process_order"),
	path('view/<str:pk>/',views.product_view,name="view"),
	path('search/',category_search.search_store,name="search-store"),


]