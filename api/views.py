from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets


from lenivastore.models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('category', 'subcategory', 'is_popular')
