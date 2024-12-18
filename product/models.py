from django.db import models
import uuid
from warehouse.models import Warehouse, Category 
from django.core.mail import send_mail

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    unit_price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sku = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    

    def __str__(self):
        return self.name
    
class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    reorder_level = models.IntegerField()

    def check_reorder_level(self):
        if self.quantity < self.product_level:
            manager_email = self.warehouse.manager.enail
            send_mail(
                subject='Inventory Alert: Low stock',
                message=f'stock for {self.product.name} in {self.warehouse.name} is below reorder level.',
                from_emails='no-reply@warehouse.com',
                recipient_list = [manager_email]
            )

    def __str__(self):
        return f'{self.product.name} in {self.warehouse.name}'
    
# class StockAudit(models.Model):
#     warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     system_quantity = models.IntegerField()  # quantity from the system
#     physical_quantity = models.IntegerField()  # quantity from physical audit
#     audit_date = models.DateTimeField(auto_now_add=True)
#     auditor = models.ForeignKey( on_delete=models.CASCADE) 

#     def check_discrepancy(self):
#         return self.system_quantity != self.physical_quantity

     
class Supplier(models.Model):
    name = models.CharField(max_length=225)
    contact_info = models.CharField(max_length=225) 
    address = models.CharField(max_length=225)
    products_supplied = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

class Shipment(models.Model):
    SHIPMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('in transit', 'In Transit'),
        ('delivered', 'Delivered'),
    ]
    shipment_number = models.CharField(max_length=225, unique=True)
    carrier = models.CharField(max_length=225)
    shipping_address = models.CharField(max_length=225)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=225, choices=SHIPMENT_STATUS_CHOICES)
    shipment_date = models.DateTimeField(auto_now_add=True)
    Delivery_date = models.DateField()

    def __str__(self):
        return self.shipment_number

