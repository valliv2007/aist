from datetime import datetime as dt
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from rest_framework import viewsets

from cupons.models import Cupon
from lenivastore.models import Product, Subcategory
from orders.models import CallBack, Order, OrderItem
from .filters import ProductFilter, SubcategoryFilter
from .mail import sent_email
from .mixins import OnlyRetriveSet, PostViewSet
from .serializers import (CallBackSerializer, CuponSerializer,
                          OrderSerializer, OrderItemListSerializer,
                          ProductSerializer, SubcategorySerializer)
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


class CuponViewSet(OnlyRetriveSet):

    queryset = Cupon.objects.filter(
        active=True, valid_from__lte=dt.today().strftime('%Y-%m-%d'),
        valid_to__gte=dt.today().strftime('%Y-%m-%d'))
    serializer_class = CuponSerializer
    lookup_field = 'code'


class OrderViewSet(PostViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(PostViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemListSerializer

    def perform_create(self, serializer):
        serializer.save()
        subject = "Новый заказ"
        order = get_object_or_404(Order, id=serializer.data[0].get('order'))
        message = render_to_string('orders/order/mail.txt', {'order': order})
        sent_email(subject, message)
        send_telegram(message)
