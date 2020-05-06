from django.contrib import admin

# Register your models here.

from store.models import *

@admin.register(Customer)
class ModelCustomer(admin.ModelAdmin):
    list_display = ['name','email']
    
# admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
    
