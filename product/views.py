from django.shortcuts import render
from .models import *
# from rest_framework.permissions import IsAuthenticated
# from warehouse.permissions import *
from .serializer import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
# from warehouse.serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer


# CREATE ITEMS
@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    # permission_class = [IsAuthenticated, IsAdmin | IsManager]
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_stock(request):
    serializer = StockSerializer(data=request.data)
    # permission_class = [IsAuthenticated, IsAdmin | IsManager]
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_supplier(request):
    serializer = SupplierSerializer(data=request.data)
    # permission_class = [IsAuthenticated, IsAdmin | IsManager]
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_shipment(request):
    serializer = ShipmentSerializer(data=request.data)
    # permission_class = [IsAuthenticated, IsAdmin | IsManager]
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET ALL ITEMS
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_stocks(request):
    stocks = Stock.objects.all()
    serializer = StockSerializer(stocks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_suppliers(request):
    suppliers = Supplier.objects.all()
    serializer = SupplierSerializer(suppliers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_shipments(request):
    shipments = Shipment.objects.all()
    serializer = ShipmentSerializer(shipments, many=True)
    return Response(serializer.data)

# UPDATE INDIVIDUAL ITEM
@api_view(['GET', 'PUT', 'DELETE'])
def product_details(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Check if the request method is GET
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    # Check if the request method is PUT
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Check if the request method is DELETE
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT', 'DELETE'])
def stock_details(request, pk):
    try:
        stock = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.data == 'GET':
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    if request.data == 'PUT':
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.data == 'DELETE':
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT', 'DELETE'])
def supplier_details(request, pk):
    try:
        supplier = Supplier.objects.get(pk=pk)
    except Supplier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.data == 'GET':
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)

    if request.data == 'PUT':
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.data == 'DELETE':
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT', 'DELETE'])
def shipment_details(request, pk):
    try:
        shipment = Shipment.objects.get(pk=pk)
    except Shipment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.data == 'GET':
        serializer = ShipmentSerializer(shipment)
        return Response(serializer.data)
    
    if request.data == 'PUT':
        serializer = ShipmentSerializer(shipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.data == 'DELETE':
        shipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# # REPORT AND ANALYTICS
# @api_view(['GET'])
# # @permission_classes([IsAuthenticated, IsAdmin])
# def stock_report(request):
#     stock_data = Stock.objects.values('product__name', 'warehouse__name').annotate(
#         total_quantity=models.Sum('quantity')
#     ).order_by('product__name')

#     return Response(stock_data)

# @api_view(['GET'])
# # @permission_classes([IsAuthenticated, IsAdmin])
# def supplier_performance_report(request):
#     supplier_data = Supplier.objects.values('name').annotate(
#         total_products=models.Count('products')
#     ).order_by('-total_products')

#     return Response(supplier_data)

