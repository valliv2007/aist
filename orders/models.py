from django.db import models
from lenivastore.models import Product
from cupons.models import Cupon
# from decimal import Decimal

from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    phone_order = PhoneNumberField(blank=False, verbose_name="Телефон")
    first_name = models.CharField(max_length=50, verbose_name="Имя", blank=False)
    # last_name = models.CharField(max_length=50, blank=True, verbose_name="Фамилия")
    email = models.EmailField(blank=True)
    # address = models.CharField(max_length=150, blank=True, verbose_name="Адрес")
    # postal_code = models.CharField(max_length=20, blank=True,verbose_name="Почтовый индекс")
    # city = models.CharField(max_length=100, blank=True, verbose_name="Город")
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Заказ создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Заказ изменен")
    # paid = models.BooleanField(default=False,  verbose_name="Оплата")
    # order_processed = models.BooleanField(default=False, verbose_name='Оплачен')
    # card_paid = models.BooleanField(default=False, verbose_name="Онлайн оплата")
    cupon = models.ForeignKey(Cupon, related_name='orders', null=True,
                              blank=True, on_delete=models.CASCADE)
    # discount = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
    order_price = models.IntegerField(verbose_name="Итоговая стоимость заказа", default=0)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)
    """
    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))
   """

    def get_total_cost_no_sale(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_order_discount(self):
        return self.get_total_cost_no_sale() - self.order_price


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class CallBack(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя", blank=False)
    phone_number = PhoneNumberField(blank=False, verbose_name="Телефон", unique=True)

    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратные звонки'
