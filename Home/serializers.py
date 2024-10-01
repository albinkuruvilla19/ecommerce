from rest_framework import serializers
from .models import Category, Products, Cart, Checkout


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='products.name')

    class Meta:
        model = Cart
        fields = ['id', 'user', 'products', 'product_name', 'product_quantity', 'created_at', 'checked_out']


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = '__all__'

