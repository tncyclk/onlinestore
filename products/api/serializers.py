from itertools import product
from django import views
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ListSerializer,DateTimeField
from products.models import Manufacturer, Product



class ManufacturerSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
            model = Manufacturer
            fields = ['id', 'name', 'location', 'active']



class ProductsSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
            model = Product
            fields = ['id', 'name', 'description', 'photo', 'price', 'shipping_cost', 'quantity']


class ManufacturerRetrieveSerializer(ModelSerializer):
    products_list = ListSerializer(
        child = ProductsSerializer(),
        source = 'products'
    )
    class Meta:
            model = Manufacturer
            fields = ['id', 'name', 'location', 'active', 'products_list']

