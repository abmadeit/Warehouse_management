from django.urls import path
from .views import *

urlpatterns = [
    #creating entries
    path('create/inventory_movement/', create_inventory_movement, name='create_inventory_movement'),
    path('create/order/', create_order, name='create_order'),
    path('create/orderproduct/', create_orderproduct, name='create_orderproduct'),
    #viewing all entries
    path('inventory_movements/', get_inventory_movements, name='get_inventory_movements'),
    path('orders/', get_orders, name='get_orders'),
    path('orderproducts/', get_orderproducts, name='get_orderproducts'),
    #viewing individual entries 
    path('order/<int:pk>/', order_details, name='order_details'),
    path('orderproduct/<int:pk>/', orderproduct_details , name='orderproduct_details'),
    path('inventory_movement/<int:pk>/', inventory_movement_details, name='inventory_movement_details'),
]
