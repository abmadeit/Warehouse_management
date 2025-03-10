from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'

class Inventory_MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory_Movement
        fields = '__all__'