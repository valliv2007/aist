from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


from lenivastore.models import Product, Subcategory
from .filters import ProductFilter, SubcategoryFilter
from .serializers import ProductSerializer, SubcategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ProductFilter


class SubcategoryViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SubcategoryFilter
