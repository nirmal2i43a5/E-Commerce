from django.contrib import admin

# Register your models here.

from store.models import *

@admin.register(Customer)
class ModelCustomer(admin.ModelAdmin):
    list_display = ['name','email']
    list_filter = ['name']
    
# admin.site.register(Customer)

@admin.register(Product)
class ModelProduct(admin.ModelAdmin):
    search_fields = ['name']
# admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
    
