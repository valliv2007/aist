from rest_framework import serializers

from lenivastore.models import Product, Subcategory


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.slug')
    subcategory = serializers.ReadOnlyField(source='subcategory.slug')

    class Meta:
        model = Product
        fields = ('__all__')


class SubcategorySerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.slug')

    class Meta:
        model = Subcategory
        fields = ('__all__')
