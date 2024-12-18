from django.shortcuts import render
from .models import *
# from rest_framework.permissions import IsAuthenticated 
# from warehouse.permissions import IsAdmin, IsManager, IsOperator
from rest_framework.decorators import api_view
from .serializer import Inventory_MovementSerializer, OrderSerializer, OrderProductSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


@api_view(['POST'])
def create_inventory_movement(request):
    serializer = Inventory_MovementSerializer(data=request.data)
    # permission_class = [IsAuthenticated, IsAdmin | IsManager]
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    # permission_class = [IsAuthenticated, IsAdmin | IsManager]
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_orderproduct(request):
    serializer = OrderProductSerializer(data=request.data)
    # permission_class = [IsAuthenticated, IsAdmin | IsManager]
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_inventory_movements(request):
    inventory_movements = Product.objects.all()
    serializer = Inventory_MovementSerializer(inventory_movements, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_orderproducts(request):
    orderproducts = OrderProduct.objects.all()
    serializer = OrderProductSerializer(orderproducts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def order_details(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def orderproduct_details(request, pk):
    try:
        orderproduct = OrderProduct.objects.get(pk=pk)
    except OrderProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OrderProductSerializer(orderproduct)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = OrderProductSerializer(orderproduct, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        orderproduct.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'DELETE'])
def inventory_movement_details(request, pk):
    try:
        inventory_movement = Inventory_Movement.objects.get(pk=pk)
    except Inventory_Movement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = Inventory_MovementSerializer(inventory_movement)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = Inventory_MovementSerializer(inventory_movement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        inventory_movement.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

    

    
#REPORT AND ANALYTICS
# @api_view(['GET'])
# # @permission_classes([IsAuthenticated, IsAdmin])
# def sales_report(request):
#     orders = Order.objects.filter(status='Shipped').values('order_date').annotate(
#         total_sales=models.Sum('total_price')
#     ).order_by('order_date')

#     return Response(orders)
