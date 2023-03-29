from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


from lenivastore.models import Product
from .filters import ProductFilter
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ProductFilter
