from rest_framework import serializers

from lenivastore.models import Product, Subcategory
from orders.models import CallBack


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.slug')
    subcategory = serializers.ReadOnlyField(source='subcategory.slug')
    quanity = serializers.ReadOnlyField(default=1)
    total_price = serializers.ReadOnlyField(source='price')

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
