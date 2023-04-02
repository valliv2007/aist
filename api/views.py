from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
from django.core.mail import get_connection, EmailMultiAlternatives
from rest_framework import viewsets


from lenivastore.models import Product, Subcategory
from orders.models import CallBack
from .filters import ProductFilter, SubcategoryFilter
from .mixins import PostViewSet
from .serializers import (CallBackSerializer, ProductSerializer, SubcategorySerializer)
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
        connection = get_connection()
        connection.open()
        subject = "Обратный звонок"
        message = f"Клиент {serializer.data.get('name')} просит перезвонить по номеру: {serializer.data.get('phone_number')}"
        email = EmailMultiAlternatives(
            subject, message, settings.EMAIL_HOST_USER, ['valliv2007@ya.ru'],
            connection=connection)
        email.send()
        connection.close()
        send_telegram(message)
