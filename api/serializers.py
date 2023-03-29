from rest_framework import serializers

from lenivastore.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.slug')
    subcategory = serializers.ReadOnlyField(source='subcategory.slug')

    class Meta:
        model = Product
        fields = ('__all__')
