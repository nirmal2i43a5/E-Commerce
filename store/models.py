from django.db import models

from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save#user object  signal create hunxa

class Customer(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
		   
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		
		
	def __str__(self):
		return self.user.username    #i use this function because i dont use null =True in use


	@receiver(post_save, sender = User)#post save paxi uend by user--for register
	def update_profile(sender,instance,created,*args,**kwargs):
     
		if created:
			Customer.objects.create(user=instance)
			instance.customer.save()


class Product(models.Model):

	category = (
		
			('Mens shoes and clothing','Mens shoes and clothing'),
			('Womens shoes and clothing','Womens shoes and clothing'),
			('Laptop','Laptop'),('Desktop','Desktop'),('Camera','Camera'),('Mobile','Mobile'),
			('Laptop accessories','Laptop accessories'),('Storage','Storage'),
			('Mobile accessories','Mobile accessories'),('Audio','Audio'),('Antivirus','Antivirus'),
			('Camera accessories','Camera accessories'),('Breakfast & Snacks','Breakfast & Snacks'),
			('Wines,beers,& spirits','Wines,beers,& spirits'),('Cooking ingredients','Cooking ingredients'),
			('Kitchen,Dining, & Bedding','Kitchen,Dining, & Bedding'),('Media,Books, & Music','Media,Books, & Music'),
			('Watches','Watches'),('Sunglasses & Eyeglasses','Sunglasses & Eyeglasses'),
			('Make up & Body care','Make up & Body care'),('Food supplements','Food supplements')
   		
			


	)
	name = models.CharField(max_length=200)
	price = models.DecimalField(default = 0, max_digits = 10,decimal_places=1)

	discount = models.DecimalField(default = 0, max_digits = 10,decimal_places=1)
	digital = models.BooleanField(default=False, null=True, blank=True)
	image = models.ImageField(upload_to='images', null=True, blank=True)
	category=models.CharField(max_length=200,null=True,choices=category)
	

	def __str__(self):
		return self.name

	@property
	def imageUrl(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
	@property
	def get_final_price_after_discount(self):
		return (self.price) -  (self.price * (self.discount)/100)
	

 


class Order(models.Model):
	customer = models.ForeignKey(
		Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)
 
 
	@property
	def get_cart_total(self):#whole orderitem total price
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 



	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 


	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	
	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	# description = models.TextField()
	

	@property
	def get_total(self):#particuler orderitem price
		total = self.quantity * self.product.price
		return total

	@property
	def get_total_discount_item_price(self):
		return self.quantity * (self.product.price * (self.product.discount)/100)

	#i use decimal field and it is not callable so i use long code 

	@property
	def get_final_price_after_discount(self):
		return (self.quantity * self.product.price) - self.quantity * (self.product.price * (self.product.discount)/100)



	@property
	def total_save_price(self):
		total_save = 0.00
		total_save = self.quantity * (self.product.price * (self.product.discount)/100)

		for price in total_save:
			total_discount_price = total_save + self.quantity * (self.product.price * (self.product.discount)/100)

		return total_save


		
		

	

	
	

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
