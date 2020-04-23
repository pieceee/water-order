from rest_framework import serializers
from .models import Order, ProductOrder


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    volume = serializers.FloatField()
    price = serializers.FloatField()
    #photo = serializers.ImageField() # передача файлов не поддерживается


class OrdersListSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    status = serializers.CharField()
    client_id = serializers.CharField()

    def __init__(self, data):
        self.status = data['status']
        self.client_id = data['client_id']
        self.access_token = data['access_token']


class CartSerializer(serializers.ModelSerializer):
    #id = serializers.UUIDField()
    #count = serializers.IntegerField()
    product_id = serializers.CharField()
    class Meta:
        model = ProductOrder
        fields = ('order_id', 'product_id', 'count')

    #def __init__(self, data):
    #    self.id = data['id']
    #    self.count = data['count']


class OrderSerializer(serializers.ModelSerializer):
    products = CartSerializer(many=True)
    class Meta:
        model = Order
        fields = ('user_id', 'place', 'date', 'status', 'products', 'id')


class AdressSerializer(serializers.Serializer):
    coords = serializers.CharField()
    place = serializers.CharField()
    comment = serializers.CharField()

    def __init__(self, data):
        self.coords = data['coords']
        self.place = data['place']
        self.comment = data['comment']
