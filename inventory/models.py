from django.db import models
from product.models import Product, Shipment
from warehouse.models import User, Warehouse
# Create your models here.

class Order(models.Model):
	order_number = models.CharField(max_length=225, unique=True) 
	customer = models.ForeignKey(User, on_delete=models.CASCADE)
	ordered_products = models.ManyToManyField(Product, through='OrderProduct') # Using through model
	total_price = models.IntegerField()
	status = models.CharField(max_length=225)
	order_date = models.DateTimeField(auto_now_add=True)
	shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE) 
	
	def __str__(self):
		return self.order_number 

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
	
    def __str__(self):
        return self.order 
    

class Inventory_Movement(models.Model):
    MOVEMENT_TYPE_CHOICES = [
        ('receiving', 'Receiving'),
        ('shipping', 'Shipping'),
        ('transferring', 'Transferring'),  
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField()  # Changed to IntegerField
    timestamp = models.DateTimeField(auto_now_add=True)
    movement_type = models.CharField(max_length=225, choices=MOVEMENT_TYPE_CHOICES)

    def __str__(self):
        if self.movement_type != 'transferring':
            return f'{self.movement_type} {self.product.name} in {self.warehouse.name}'
        return f'{self.movement_type} {self.product.name} to {self.warehouse.name}'