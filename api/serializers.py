from rest_framework import serializers

from cupons.models import Cupon
from lenivastore.models import Product, Subcategory
from orders.models import CallBack, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.slug')
    subcategory = serializers.ReadOnlyField(source='subcategory.slug')
    quantity = serializers.ReadOnlyField(default=1)
    total_price = serializers.ReadOnlyField(source='price')
    is_in_bag = serializers.ReadOnlyField(default=1)

    class Meta:
        model = Product
        fields = ('__all__')


class SubcategorySerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.slug')

    class Meta:
        model = Subcategory
        fields = ('__all__')


class CallBackSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallBack
        fields = ('__all__')


class CuponSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Cupon
        fields = ('id', 'code', 'discount')

    def get_discount(self, obj):
        return (1 - obj.discount/100)


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'phone_order', 'first_name', 'email', 'cupon', 'order_price')


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('__all__')


class OrderItemListSerializer(serializers.ListSerializer):
    child = OrderItemSerializer()

    def create(self, validated_data):
        return [OrderItem.objects.create(**item) for item in validated_data]
