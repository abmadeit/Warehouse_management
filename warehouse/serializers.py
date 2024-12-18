from typing import Any, Dict
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# class RoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Role
#         fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Warehouse
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =  '__all__'

# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     email = serializers.EmailField()
#     name = serializers.CharField()

#     def validate(self, attrs):
#         try:
#             user = CustomUser.objects.get(email=attrs['email'])
#             if user.name != attrs['name']:
#                 raise serializers.ValidationError('Invalid name or email')
#             attrs['username'] = user.username
#         except CustomUser.DoesNotExist:
#             raise serializers.ValidationError('Invalid name or email')
        
#         return super().validate(attrs)