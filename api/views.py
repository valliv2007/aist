from datetime import datetime as dt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from cupons.models import Cupon
from lenivastore.models import Product, Subcategory
from orders.models import CallBack
from .filters import ProductFilter, SubcategoryFilter
from .mail import sent_email
from .mixins import PostViewSet
from .serializers import (CallBackSerializer, CuponSerializer, ProductSerializer, SubcategorySerializer)
from .telegram import send_telegram


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


class CallBackViewSet(PostViewSet):
    queryset = CallBack.objects.all()
    serializer_class = CallBackSerializer

    def perform_create(self, serializer):
        serializer.save()
        subject = "Обратный звонок"
        message = f"Клиент {serializer.data.get('name')} просит перезвонить по номеру: {serializer.data.get('phone_number')}"
        sent_email(subject, message)
        send_telegram(message)


class CuponViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Cupon.objects.filter(
        active=True, valid_from__lte=dt.today().strftime('%Y-%m-%d'),
        valid_to__gte=dt.today().strftime('%Y-%m-%d'))
    serializer_class = CuponSerializer
    lookup_field = 'code'
