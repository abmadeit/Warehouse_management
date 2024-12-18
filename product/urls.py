from django.urls import path
from .views import *

urlpatterns = [
    path('create/product/', create_product, name='create_product'),
    path('create/stock/', create_stock, name='create_stock'),
    path('create/supplier/', create_supplier, name='create_supplier'),
    path('create/shipment/', create_shipment, name='create_shipment'),
    #viewing all entries
    path('products/', get_products, name='get_products'),
    path('stocks/', get_stocks, name='get_stocks'),
    path('suppliers/', get_suppliers, name='get_suppliers'),
    path('shipments/', get_shipments, name='get_shipments'),
    #viewing individual entries
    path('product/<int:pk>/', product_details, name='product_details'),
    path('stock/<int:pk>/', stock_details, name='stock_details'),
    path('supplier/<int:pk>/', supplier_details, name='supplier_details'),
    path('shipment/<int:pk>/', shipment_details, name='shipment_details'),
]