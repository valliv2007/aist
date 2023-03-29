import django_filters

from lenivastore.models import Product


class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__slug')
    subcategory = django_filters.CharFilter(field_name='subcategory__slug')
    is_popular = django_filters.BooleanFilter(field_name='is_popular')
    available = django_filters.BooleanFilter(field_name='available')

    class Meta:
        model = Product
        fields = ('subcategory', 'is_popular', 'category', 'available')
